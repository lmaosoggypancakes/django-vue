<template>
  <div>
    <Navbar :is_auth='is_user' @is_user='login' :user="user" @update='update'/>
    <router-view @is_user='login' @update='login_from_reg' />
  </div>
</template>
<style lang="scss">
@import "../node_modules/bulma";
</style>
<script>
import Navbar from "./components/Navbar.vue"
export default {
  name: "app",
  mounted() {
    this.ValidateUser()
  },
  methods: {
      login_from_reg(user) {
        this.user = JSON.parse(user)
        this.is_user = true
      },
      update(user) {
        console.log('updated')
        this.user = user
      },
      login(value) {
        this.is_user = value
        console.log("event received")
      },
      ValidateUser() {
        var user;
        try {
          user = JSON.parse(window.localStorage.getItem("user"));
        } catch(e) {
          user = ''
        }
        console.log(user)
        this.user = user
        fetch("http://127.0.0.1:8000/api/login", {
          method: "POST",
          body: JSON.stringify({
            username: user.username,
            password: user.password,
          })
          }).then(res => res.json()).then(data => {
            if (JSON.stringify(data.user) !== JSON.stringify(user))
            {
              this.$router.push("login")
              this.is_user = false;
              console.log("not logged in")
            } else {
              this.is_user = true;
              console.log("yes logged in");
              }
          })
    },
  },
  components: {
    Navbar
  },
  data() {
    return {
      is_user: false,
      user: Object
    }
  }
}
</script>
