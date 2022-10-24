<script >
import { RouterLink, RouterView } from 'vue-router'
import TextEmotion from './components/TextEmotion.vue'
import UserHeader from './components/UserHeader.vue'


export default {
  name:'App',
  components:{
    TextEmotion,
    UserHeader,

  }
}

</script>

<template>
  
     <UserHeader/>
   

  <div class="row">
  <TextEmotion/>
  </div>
</template>
