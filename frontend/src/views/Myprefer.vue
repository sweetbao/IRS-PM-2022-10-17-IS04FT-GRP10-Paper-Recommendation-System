<script>
import axios from 'axios'
import { reactive, onMounted, toRefs, ref } from 'vue'
import PaperRecommend from '../components/PaperRecommend.vue';
import router from '../router'






export default {
  name: 'Myprefer',
  components: {
    PaperRecommend
  },


  setup() {


  }
}
</script>


<template>

  <PaperRecommend />
</template>