<template>
<div>
    <form @submit.prevent="register()" method="post">
        <div class="columns">
            <div class="column">
                <div class="field">
                    <label class="label">First Name</label>
                    <div class="control">
                        <input class="input" type="text" v-model="first">
                    </div>
                </div>
            </div>
            <div class="column">
                <div class="field">
                    <label class="label">Last Name</label>
                    <div class="control">
                        <input class="input" type="text" v-model="last">
                    </div> 
                </div>
            </div>
        </div>



        <div class="field">
            <label class="label">Username</label>
            <div class="control has-icons-left has-icons-right">
                <input :class="usernameClass" type="text" placeholder="Make it unique!" v-model="username" @keyup="checkUsername()" id="username_reg" autocomplete="off">
                <span class="icon is-small is-left">
                <i class="fas fa-user"></i>
                </span>
                <span class="icon is-small is-right" id="check-username-holder">
                <i :class="usernameIconClass"></i>
                </span>
            </div>
            <p :class="usernameAvailible">{{username_ready}}</p>
        </div>
        <div class="field">
            <label class="label">Email</label>
            <div class="control  has-icons-left has-icons-right">
                <input :class="emailClass" type="text" placeholder="vue-is-awesome@example.com" v-model="email" @keyup="checkEmail()" id="email_reg">
                <span class="icon is-small is-left">
                <i class="fas fa-at"></i>
                </span>
            </div>
        </div>
    
        <div class="field">
            <label class="label">Password</label>
            <div class="control has-icons-left has-icons-right">
                <input type="password" class="input" v-model="password">
                <span class="icon is-small is-left">
                <i class="fas fa-key"></i>
                </span>
            </div>
        </div>

        <div class="field">
            <label class="label">Profile Picture</label>
            <div class="control has-icons-left has-icons-right">
                <input type="url" class="input" v-model="pfp">
                <span class="icon is-small is-left">
                <i class="fas fa-images"></i>
                </span>
            </div>
        </div>
        <button class="button is-primary" type="submit" :disabled="!(usernameReady === true && emailReady === true)">Register</button>
    </form>
</div>
</template>
<style scoped>
@import '../../node_modules/bulma';

</style>
<script>
export default {
    name: "Register",
    data() {
        return {
            username: '',
            password: '',
            first: '',
            last: '',
            email: '',
            pfp: '',
            emailReady: '',
            usernameReady: '',
            usernameClass: 'input',
            usernameIconClass: '',
            usernameAvailible: '',
            username_ready: '',
            emailClass: 'input'
        }
    },
    methods: {
        checkEmail() {
            const domains = [
                '.com',
                '.net',
                '.org'
            ]
            if (!(this.email.includes('@'))) return;
            var test = this.email.substr(this.email.length - 4)
            for (var i = 0; i < 3; i++) {
                let j = domains[i];
                console.log(test)
                if (test === j) {
                    this.emailReady = true;
                    this.emailClass = 'input is-success'
                    return;
                }
            }
            this.emailReady = false;
            this.emailClass = 'input is-danger'
            return;
        },
        checkUsername() {
            fetch("http://127.0.0.1:8000/api/check", {
                method: "POST",
                body: JSON.stringify({
                    'name': this.username
                })
            }).then(res => res.json()).then(data => {
                console.log(data.is_ok)
                this.usernameReady = data.is_ok
                if (data.is_ok === false)  {
                    this.usernameClass = 'input is-danger'
                    this.usernameIconClass = 'fas fa-times',
                    this.usernameAvailible = 'help is-danger',
                    this.username_ready = 'This username is already taken! :('
                    }
                else {
                    this.usernameClass = 'input is-success'
                    this.usernameIconClass = 'fas fa-check',
                    this.usernameAvailible = 'help is-success',
                    this.username_ready = 'This username is availible'
                    }
            })
        },
        register() {
            fetch("http://127.0.0.1:8000/api/register", {
                method: "POST",
                body: JSON.stringify({
                    username: this.username,
                    first: this.first,
                    last: this.last,
                    email: this.email,
                    password: this.password,
                    pfp: this.pfp,
                })
            }).then(res => res.json()).then(data => {
                console.log(JSON.stringify(data.user))
                window.localStorage.setItem('user', JSON.stringify(data.user))
                this.$emit('update', JSON.stringify(data.user))
                this.$router.push('/')
            })
        }
    },

}
</script>