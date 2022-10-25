<script >
import { RouterLink, RouterView } from 'vue-router'
import PaperRecommend from './components/PaperRecommend.vue'
import UserHeader from './components/UserHeader.vue'
import Main from './components/Main.vue'

export default {
  name:'App',
  components:{
    Main,
    UserHeader,

  }
}

</script>

<template>
  
     <UserHeader/>
   

  <div class="row">
  <Main/>
  </div>
</template>
