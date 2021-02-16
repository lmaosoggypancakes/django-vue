<template>
<div>
    <div class="card">
        <div class="card-image">
            <figure class="image is-4by3">
            <img :src="i.image" alt="Placeholder image">
            </figure>
        </div>
        <div class="card-content">
            <div class="media">
            <div class="media-left">
                <figure class="image is-48x48">
                <img :src="i.host.image" alt="Placeholder image">
                </figure>
            </div>
            <div class="media-content">
                <p class="title is-4">{{i.title}}</p>
                <p class="subtitle is-6">{{i.host.username}}</p>
            </div>
            </div>

            <div class="content">
            {{i.desc}}<a>@bulmaio</a>.
            <br>
            <time>Ends at {{i.end}}</time>  
            <hr>
            <button class="button is-primary">View Post</button>
            </div>
        </div>
    </div>
    <hr>
</div>
</template>
<script>
export default {
    name: "Post",
    props: {
        i: Object
    }
}
</script>
<style scoped>
@import "../../node_modules/bulma";
</style>