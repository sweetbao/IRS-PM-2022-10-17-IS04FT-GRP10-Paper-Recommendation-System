<script>
import axios from 'axios'
import { reactive, onMounted, toRefs, ref } from 'vue'
import router from '../router'






export default {
  name: 'Myprefer',
  components: {
    
  },


  setup() {
    let base_url = "http://127.0.0.1:8000/api/UserPrefer/"
    const state = reactive({
      Keyword_list: [],
      Domain:''
    });

    const getMyprefer = () => {
      axios.get(base_url + "?userid=" + localStorage.getItem("user_id")).then(res => {
      
        state.Keyword_list = res.data;
        
        if(state.Keyword_list!="")
       {state.Domain=state.Keyword_list[0].Domain;
      
      
      } 
      }).catch(err => {
        console.log(err);
      })
      
    };

    const Reset = () => {
      axios.delete(base_url + "?userid=" + localStorage.getItem("user_id")).then(res => {
        
       alert("Reset Succeeded");
       router.push({ name: 'Home' })
      }).catch(err => {
        console.log(err);
      })
    };

    onMounted(() => {
      getMyprefer()
    });

    return {
      ...toRefs(state),
      getMyprefer,
      Reset
    }
  }
}
</script>


<template>
       <h4>Domain:{{Domain}}</h4> 
<ol id="Keywords">
  <li v-for="item in Keyword_list">
    {{item.Keywords}}
  </li>
</ol>

<div class="tim-title" style="text-align:right">
  <button class="btn btn-info" type="submit"
                  @click="Reset()">Reset</button>
</div>
</template>