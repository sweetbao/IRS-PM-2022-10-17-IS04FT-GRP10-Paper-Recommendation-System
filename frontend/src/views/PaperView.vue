
<script>
import axios from 'axios'
import { reactive, onMounted, toRefs, ref } from 'vue'
import PaperRecommend from '../components/PaperRecommend.vue';
import router from '../router'
import { useRoute } from 'vue-router'






export default {
  name: 'PaperView',
  props: ['keywords'],
  components: {
    PaperRecommend
  },
  methods: {
    GetURL() {
      window.scrollTo(0, 0);
    },
    redirect(link){
      window.location.href=link;
    }
  },

  setup() {
    let base_url = "http://127.0.0.1:8000/api/"
    const route = useRoute();

    const state = reactive({
      Paper_list: [],
      SelectPapers: [],
    });

    const Getpaperlist = () => {
      axios.post(base_url + "testId/", state.SelectPapers).then(res => {
    
        state.Paper_list = res.data;
      }).catch(err => {
        console.log(err)
      });
    };

    onMounted(() => {
      let selecttopic = route.params.keywords;
      const myArray = selecttopic.split(",");
      state.SelectPapers = myArray;
      Getpaperlist();
    });

    return {
      ...toRefs(state),
      Getpaperlist
    }

  }

}
</script>

<style>
:root {
  scroll-behavior: smooth;
}

.stt {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
  width: 3rem;
  height: 3rem;
  border-radius: 50%;
  background: rgb(128, 128, 255) url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 384 512'%3E%3Cpath fill='currentColor' d='M352 352c-8.188 0-16.38-3.125-22.62-9.375L192 205.3l-137.4 137.4c-12.5 12.5-32.75 12.5-45.25 0s-12.5-32.75 0-45.25l160-160c12.5-12.5 32.75-12.5 45.25 0l160 160c12.5 12.5 12.5 32.75 0 45.25C368.4 348.9 360.2 352 352 352z'%3E%3C/path%3E%3C/svg%3E") center no-repeat;
  box-shadow: 0 0.25rem 0.5rem 0 gray;
  opacity: 0.7;
}

.stt:hover {
  opacity: 0.8;
}

.stt:focus {
  opacity: 0.9;
}

.stt:active {
  opacity: 1;
}

figure { 
  position: absolute;
  margin: auto;
  top: 0; bottom: 0; left: 0; right: 0;
  width: 6.250em; height: 6.250em;
  animation: rotate 2.4s linear infinite;
}
.white { 
  top: 0; bottom: 0; left: 0; right: 0; 
  background: white; 
  animation: flash 2.4s linear infinite;
  opacity: 0;
}
.dot {
  position: absolute;
  margin: auto;
  width: 2.4em; height: 2.4em;
  border-radius: 100%;
  transition: all 1s ease;
}
.dot:nth-child(2) { top: 0; bottom: 0; left: 0; background: #FF4444; animation: dotsY 2.4s linear infinite; }
.dot:nth-child(3) { left: 0; right: 0; top: 0; background: #FFBB33; animation: dotsX 2.4s linear infinite; }
.dot:nth-child(4) { top: 0; bottom: 0; right: 0; background: #99CC00; animation: dotsY 2.4s linear infinite; }
.dot:nth-child(5) { left: 0; right: 0; bottom: 0; background: #33B5E5; animation: dotsX 2.4s linear infinite; }

@keyframes rotate {
  0% { transform: rotate( 0 ); }
  10% { width: 6.250em; height: 6.250em; }
  66% { width: 2.4em; height: 2.4em; }
  100%{ transform: rotate(360deg); width: 6.250em; height: 6.250em; }
}

@keyframes dotsY {
  66% { opacity: .1; width: 2.4em; }
  77%{ opacity: 1; width: 0; }
}
@keyframes dotsX {
  66% { opacity: .1; height: 2.4em;}
  77%{ opacity: 1; height: 0; }
}

@keyframes flash {
  33% { opacity: 0; border-radius: 0%; }
  55%{ opacity: .6; border-radius: 100%; }
  66%{ opacity: 0; }
}
</style>
<template>
  <div v-if="Paper_list.length==0" style="margin-top:25%;margin-left: 25%;">
<figure>
  <div class="dot white"></div>
  <div class="dot"></div>
  <div class="dot"></div>
  <div class="dot"></div>
  <div class="dot"></div>
</figure>
</div>

  <div class="content" id="top" >
<div>
    <ol id="breathe-horizontal" start="1">
      <li v-for="item in Paper_list" :key="item.fields.url" class="arxiv-result">
        <div class="is-marginless">
          <p class="list-title is-inline-block"><a :helf="item.fields.link" class="link external" @click="redirect(item.fields.link)" >{{ item.fields.title }}</a></p>
          <p class="authors"> <span class="has-text-black-bis has-text-weight-semibold">Authors: </span>
            <label>{{ item.fields.author }}</label>
          </p>
          <p class="abstract mathjax">
            <span class="search-hit">Abstract: </span>
            <span class="abstract-short has-text-grey-dark mathjax" style="display: inline;">{{ item.fields.abstract }}
            </span>
          </p>

          <p class="is-size-7"><span class="has-text-black-bis has-text-weight-semibold">Submitted </span>
            {{ item.fields.publishTime }}


          <p class="comments is-size-7">

            <span class="has-text-black-bis has-text-weight-semibold">Comments: </span>
            <span class="has-text-grey-dark mathjax">{{ item.fields.comment }}</span>
          </p>

          </p>
        </div>
        <br>
      </li>
    </ol>


    <a @click="GetURL()" class="stt" title="Back to Top"></a>
  </div>
</div>

</template>



