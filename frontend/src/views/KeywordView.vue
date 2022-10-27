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
    let base_url = "http://127.0.0.1:8000/api/";
    const route = useRoute();
    const Myprefer_blank = { Domain: '', Keywords: '', PaperID: 0, comment: '', UserID: 0 }

    const state = reactive({
      Paper_list: [],
      SelectPapers: [],
      Myprefer_list: [],
      selecttopic: "",
      domain: ""
    });



    const saveMyprefer = () => {
      state.SelectPapers.forEach(element => {
        
        element=element.replace(/'/g, '"')

        let obj = JSON.parse(element);
        let newdata = {
          Domain: state.selecttopic,
          Keywords: obj.Keywords,
          PaperID: obj.PaperID,
          comment: obj.comment,
          UserID: localStorage.getItem('user_id')
        };
        console.log(newdata);
        axios.post(base_url + "UserPrefer/", newdata).then(() => {
          router.push({ name: 'Paper' })
        }).catch(err => {
          console.log(err)
        });
      })
    }
    
  

    

    



    onMounted(() => {
      let selecttopic = route.params.topic;
      const myArray = selecttopic.split("(");
      state.domain = myArray[0];
      state.selecttopic = myArray[1]
    });

    return {
      ...toRefs(state),
      saveMyprefer
    }

  },
  methods: {
    gotoPaper() {
     
    },

  },

}

</script>

<template>
  <div class="wrapper">
    <div class="main">
      <div class="section">
        <div class="container tim-container">
          <div class="tim-title">
            <p>Selected topic: {{ selecttopic }}</p>
            <h4>Choose one or more keywords combination you like</h4>
          </div>
          <input type="checkbox" value="{'Keywords':'test1','PaperID':'1','comment':'test'}" id="markcheckbox1"
            v-model="SelectPapers">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="{'Keywords':'test2','PaperID':2,'comment':'test'}" id="markcheckbox1"
            v-model="SelectPapers">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>
          <input type="checkbox" value="{'Keywords':'test3','PaperID':3,'comment':'test'}" id="markcheckbox1"
            v-model="SelectPapers">
          <label class="mark" for="markcheckbox1">markcheckbox1</label>
          <br>


          <p>Keywords: {{ SelectPapers }}</p>
        </div>
        <div class="row">
          <div class="col-md-8 col-md-offset-2">
            <div><a @click="saveMyprefer()"><input type="submit" value="Save as my prefer" /></a></div>
            <div><a @click="gotoPaper()"><input type="submit" value="submit" /></a></div>
          </div>
        </div>
      </div>
      <br />
    </div>

  </div>

  <!-- end buttons div -->








</template>

