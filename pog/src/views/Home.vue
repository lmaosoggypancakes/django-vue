<template>
  <div>
    <div class="columns">
        <div class="column"></div>
        <div class="column">
          <Post v-for="i in listings" :i="i" v-bind:key="i"/>
        </div>
        <div class="column"></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Post from "../components/Post.vue"
export default {
  name: "Home",
  data() {
    return {
      username: '',
      password: '',
      listings: [],
      user: {},
    }
  },
  mounted() {
    console.log(window.localStorage.getItem('user'))
    if (window.localStorage.getItem('user') === "") {this.$router.push('/login')}
    this.getAuctions()
  },
  methods: {
    getAuctions() {
      axios.get("http://127.0.0.1:8000/api/all").then(data => {
        console.log(data)
        this.listings = data.data
      })
    }
  },
  components: {
    Post
  }
};
</script>
