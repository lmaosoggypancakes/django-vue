<template>
    <form @submit.prevent="login()">
        <input type="text" v-model="username">
        <br>
        <input type="text" v-model="password">
        <button type="submit" id="login" class="button is-primary" :disabled="!(username && password)">Login</button>
    </form>
</template>
<script>
export default {
  name: "login",
  data() {
    return {
      username: '',
      password: '',
      user: {}
    }
  },
  methods: {
    login() {
      document.querySelector("#login").className = 'button is-primary is-loading'
      fetch("http://127.0.0.1:8000/api/login", {
        method: "POST",
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        })
      }).then(res => res.json()).then(data => {
        if (data.valid === 'true') {
          this.$emit('is_user', true)
          this.$emit('update', JSON.stringify(data.user))
          this.$router.push("/")
        }
        else {
          alert(data.message)
          document.querySelector("#login").className = 'button is-primary'
        }
        window.localStorage.setItem("user", JSON.stringify(data.user))
        this.user = data.user
      })
    }
  }
}
</script>
<style lang="scss" scoped>
@import "../../node_modules/bulma";
</style>