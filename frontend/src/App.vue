<script >
import { RouterLink, RouterView } from 'vue-router'
import UserHeader from './components/UserHeader.vue'
import router from './router';

export default {
  name: 'App',
  components: {
    UserHeader,

  }
}

</script>

<template>

  


  <div class="row">
    <UserHeader />
    <RouterView />
  </div>
</template>
