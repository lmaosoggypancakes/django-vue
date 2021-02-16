<template>
<nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="/">
      <i class="fas fa-bullhorn"></i>
    </a>

    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbarBasicExample" class="navbar-menu">
    <div class="navbar-start">
      <a class="navbar-item"  @click="$router.push('/')">
        Home
      </a>

      <a class="navbar-item">
        {{user.username}}
      </a>

      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          More
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            About
          </a>
          <a class="navbar-item">
            Jobs
          </a>
          <a class="navbar-item">
            Contact
          </a>
          <hr class="navbar-divider">
          <a class="navbar-item">
            Report an issue
          </a>
        </div>
      </div>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <a class="button is-light" @click="logout()" v-if='is_auth === true'>
            Log out
          </a>
          <a class="button is-light" @click="$router.push('/login')" v-if='is_auth === false'>
            Login
          </a>
          <a class="button is-light" @click="$router.push('/register')" v-if='is_auth === false'>
            Register
          </a>
        </div>
      </div>
    </div>
  </div>
</nav>
</template>
<style scoped>
@import "../../node_modules/bulma";
</style>
<script>
export default {
    name: "Navbar",
    props: {'is_auth': Boolean,
            'user': Object},
    methods: {
      logout() {
        window.localStorage.setItem('user', '');
        this.$router.push('/login')
        this.$emit('is_user', false)
        this.$emit('update', '')
      }
    }
}
</script>