<script>
import axios from 'axios'
import { reactive, onMounted, toRefs, ref } from 'vue'
import Main from '../components/Main.vue';
import router from '../router'
import { useRoute } from 'vue-router'





export default {
  name: 'KeywordView',

  components: {
    Main
  },


  setup() {
    let base_url = "http://127.0.0.1:8000/api/PaperRecommend/";
    const route = useRoute();
    
   
    const state = reactive({
      Paper_list: [],
      selecttopic:"",
      domain: ""
    });


    onMounted(() => {
      let selecttopic = route.params.topic;
      const myArray =selecttopic.split("(");
      state.domain=myArray[0];
      state.selecttopic=myArray[1]
    });

    return {
      ...toRefs(state),
      
    }

  },
  methods: {
    gotoPaper() {
      router.push({ name: 'Paper' })
    }

  },

}

</script>

<template>
  <div class="wrapper">
    <div class="main">
      <div class="section">
        <div class="container tim-container">
          <div class="tim-title">
            <p>Select topic: {{selecttopic }}</p> 
            <h2>Choose one or more topics you like</h2>
          </div>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="markcheckbox1" id="markcheckbox1">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <br>
          <a @click="gotoPaper()"><input type="submit" value="submit" /></a>

        </div>
        <div class="row">
          <div class="col-md-8 col-md-offset-2">

          </div>
        </div>
        <br />
        <div class="row">

        </div>
      </div>
      <div class="tim-title">

      </div>

    </div>
  </div>
  <div class="tim-title">

  </div>
  <div class="row">

  </div>

  <!-- end buttons div -->








</template>

