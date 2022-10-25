<script>
import axios from 'axios'
import { reactive, onMounted, toRefs ,ref } from 'vue'
import { useRouter,useRoute } from 'vue-router';






export default {
  name: 'Main',

 

  setup() {
    const router=useRouter()
    const twoclass =(()=>{
        router.push({
            name:twoclass
        })
    })

    return{
        twoclass
    }

  }
}

</script>

<template>
 <div>
   
  </div>

   <!-- 表格开始 -->
  <nav class="navbar navbar-ct-transparent" role="navigation-demo" id="demo-navbar">
  <div class="container">
    <!-- Brand and toggle get grouped for better mobile display -->

    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navigation-example-2">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a href="http://www.creative-tim.com">
           <div class="logo-container">
                
            </div>
      </a>
    </div>

<!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="navigation-example-2">
      <ul class="nav navbar-nav navbar-right">
        
       </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-->
</nav>


<div class="wrapper">
    <div class="demo-header demo-header-image">
            <div class="motto">
                <h1 class="title-uppercase">Find your interested paper</h1>
                <h3>Help yourself to find a new world！</h3>
            </div>
    </div>

    <div class="main">
        <div class="section">
         <div class="container tim-container">
            <div class="tim-title">
                <h2>Basic Research Area</h2>
            </div>

            <div id="buttons">
                    <div class="tim-title">
               
                            <small> Pick one topic that you are interestd in </small>
                     
                    </div>
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
                      
                    <a href="twoclass.html" target="_blank"><input type="submit" value="submit" /></a>
                    </div>
                    
                        </div>
                    </div>
                    <div class="tim-title">
                  
                    </div>
                    <div class="row">
                     
                        </div>
                    </div>
            </div>
        <!-- end buttons div -->

            

            </div>

 

 
</template>

