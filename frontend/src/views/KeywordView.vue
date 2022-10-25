<script>
import axios from 'axios'
import { reactive, onMounted, toRefs, ref } from 'vue'
import Main from '../components/Main.vue';
import router from '../router'






export default {
  name: 'KeywordView',
  components: {
    Main
  },


  setup() {


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

