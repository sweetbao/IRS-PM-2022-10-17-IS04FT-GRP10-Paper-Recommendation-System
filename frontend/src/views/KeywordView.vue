<script>
import axios from 'axios'
import { reactive, onMounted, toRefs } from 'vue'
import Main from '../components/Main.vue'
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
      domain: "",
      Cansaveprefer: "",
      UserID: "",
      PaperID: []
    });

    const getKeywords = () => {
      axios.get(base_url + "PaperRecommend/?domain=" + state.domain).then(res => {
        state.Paper_list = res.data;
        state.SelectPapers=[];
        state.Myprefer_list=[];
        state.PaperID=[];
      }).catch(err => {
        console.log(err);
      })

    };

    const getuserinfo = () => {
      state.Cansaveprefer = localStorage.getItem('HasPrefer');
      state.UserID = localStorage.getItem('user_id');

    };

    const saveMyprefer = () => {
      if (state.SelectPapers[0] != null) {
        state.SelectPapers.forEach(element => {

          element = element.replace(/'/g, '"')

          let obj = JSON.parse(element);
          state.PaperID.push(obj.PaperID.slice(obj.PaperID.slice(0, obj.PaperID.length - 2).lastIndexOf("/") + 1, obj.PaperID.length - 1));
          let newdata = {
            Domain: state.selecttopic,
            Keywords: obj.Keywords,
            PaperID: Number(obj.PaperID.slice(obj.PaperID.slice(0, obj.PaperID.length - 2).lastIndexOf("/") + 1, obj.PaperID.length - 1)),
            comment: "Done",
            UserID: Number(localStorage.getItem('user_id'))
          };
    
          axios.post(base_url + "UserPrefer/", newdata).then(() => {
            state.PaperID = state.PaperID.join(',');
            alert('saved succeeded');
            router.push({ name: 'Paper', params:{"keywords":state.PaperID}}) 
          }).catch(err => {
            console.log(err)
          });
        })
      }
      else { alert("please select at least one") }
    };

    const checkcango = () => {

      if (state.SelectPapers[0] != null) {
        state.SelectPapers.forEach(element => {

          element = element.replace(/'/g, '"')

          let obj = JSON.parse(element);
          state.PaperID.push(obj.PaperID.slice(obj.PaperID.slice(0, obj.PaperID.length - 2).lastIndexOf("/") + 1, obj.PaperID.length - 1));
        })
  
        state.PaperID = state.PaperID.join(',');
         router.push({ name: 'Paper', params:{"keywords":state.PaperID}}) 
      }
      else {
        alert("please select at least one")
      }
    };









    onMounted(() => {
      let selecttopic = route.params.topic;
      const myArray = selecttopic.split("(");
      state.domain = myArray[0];
      state.selecttopic = myArray[1];
      getuserinfo();
      getKeywords();
    });

    return {
      ...toRefs(state),
      saveMyprefer,
      getKeywords,
      getuserinfo,
      checkcango
    }

  },


}
</script>


<style>

</style>


<template>
  <div class="wrapper">
    <div class="main">
      <div class="section">
        <div class="container tim-container">
          <div class="tim-title" style="display:flex ;align-items: center;" @submit.prevent="submitFunc">
            <p style="width: fit-content;">Selected topic: {{ selecttopic }}</p>
            <button style="font-size:24px;margin-left: auto;" class="btn btn-info" @click="getKeywords()">Refresh <i
                class="fa fa-refresh"></i></button>

          </div>
          <h4>Choose one or more keywords combination you like</h4>

          <ul id="Keywords">
            <li v-for="item in Paper_list" :key="item.url">

              <label :ref_for="item.url" class="mark">
                <input :id="item.url" :value="'{\'PaperID\':\'' + item.url + '\'' + '\,\'Keywords\':\'' + item.keywords + '\'}'"
                  type="checkbox" v-model="SelectPapers">{{ item.keywords.replace(/,/g, ", ") }}</label>
              <br>
            </li>
          </ul>

        </div>
        <div class="row">
          <div class="col-md-8 col-md-offset-2" style="display:flex;">
            <div v-if="UserID != null" style="text-align:left ;width:50% ;"><a @click="saveMyprefer()">
                <input :disabled="Cansaveprefer != ''" type="submit" value="Save as my prefer"></a></div>


            <div style="text-align:right ;width:50% ;"><a @click="checkcango()"><input type="submit"
                  value="submit" /></a></div>
          </div>
        </div>
      </div>
      <br />
    </div>

  </div>

  <!-- end buttons div -->








</template>

