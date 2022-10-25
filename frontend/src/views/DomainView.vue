<script>
import axios from 'axios'
import { reactive, onMounted, toRefs, ref } from 'vue'
import Main from '../components/Main.vue';
import router from '../router'





export default {
    name: 'DomainView',
    components: {
        Main
    },


    setup() {


    },
    methods: {
        gotokeyword() {
            router.push({ name: 'Keyword' })
        }

    },


}
</script>

<template>
    <div>
        <Main />
    </div>
    <div>
        <div class="main">
            <div class="section">
                <div class="container tim-container">
                    <div class="tim-title">
                        <h4>Basic Research Area</h4>
                        <small> Pick one topic that you are interestd in </small>

                    </div>

                    <div id="buttons">

                        <div class="row">
                            <div class="col-md-8 col-md-offset-2">
                                <button href="#fakelink" class="btn">Default</button>
                                <button href="#fakelink" class="btn btn-primary">Primary</button>
                                <button href="#fakelink" class="btn btn-info">Info</button>
                                <button href="#fakelink" class="btn btn-success">Success</button>
                                <button href="#fakelink" class="btn btn-warning">Warning</button>
                                <button href="#fakelink" class="btn btn-danger">Danger</button>
                                <button href="#fakelink" class="btn btn-neutral">Neutral</button>
                            </div>
                        </div>
                        <br />
                        <div class="row">
                            <div class="col-md-8 col-md-offset-2">
                                <button href="#fakelink" class="btn btn-fill">Default</button>
                                <button href="#fakelink" class="btn btn-fill btn-primary">Primary</button>
                                <button href="#fakelink" class="btn btn-fill btn-info">Info</button>
                                <button href="#fakelink" class="btn btn-fill btn-success">Success</button>
                                <button href="#fakelink" class="btn btn-fill btn-warning">Warning</button>
                                <button href="#fakelink" class="btn btn-fill btn-danger">Danger</button>
                                <button href="#fakelink" class="btn btn-fill btn-neutral">Neutral</button>
                            </div>
                        </div>
                        <div class="tim-title">

                            <a @click="gotokeyword()"><input type="submit" value="submit" /></a>
                        </div>

                    </div>
                </div>
                <div class="tim-title">

                </div>
                <div class="row">

                </div>
            </div>
        </div>
    </div>

</template>
