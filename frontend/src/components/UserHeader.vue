<script>
import axios from 'axios'
import { reactive, onMounted, toRefs } from 'vue'
import router from '../router'

export default {
  name: 'UserHeader',
  methods: {
    gotoMyprefer() {
      router.push({ name: 'Myprefer' })
    },
   
      gotoDomain() {
        router.push({ name: 'Home' })
      }

  },
  setup() {
    let base_url = "http://127.0.0.1:8000/";




    const state = reactive({
      token: "",
      user_id: 0,
      name: "",
      account: { username: "", password: "" }
    });

    const LoginUser = () => {
      axios.post(base_url + "login/", state.account,
        {
          headers: {
            'Content-Type': 'application/json; charset=UTF-8',
          }
        }
      ).then(response => {
        state.user_id = response.data.token
        state.token = response.data.token
        state.name = response.data.user_name
        localStorage.setItem('token', response.data.token)
        localStorage.setItem('user_id', response.data.user_id)
        localStorage.setItem('name', response.data.user_name)
        window.location.href = '/'
      }
      ).catch(err => {
        alert("Incorrect username/password");
      })
    };

    const RegisterUser = () => {
      axios.post(base_url + "register/", state.account,
        {
          headers: {
            'Content-Type': 'application/json; charset=UTF-8',
          }
        }
      ).then(response => {

        if (response.data.status) {
          alert("user " + response.data.user_name + " created")
          state.account.password = "";
        }
        else { alert("Duplicated username"); }
      }
      ).catch(err => {
        alert("Register failed");
      })
    };

    const logout = () => {
      state.user_id = 0;
      state.token = "";
      state.name = "";
      state.account.username = "";
      state.account.password = "";
      localStorage.removeItem('token');
      localStorage.removeItem('user_id');
      localStorage.removeItem('name');
      window.location.href = '/';
    };

    


    onMounted(() => {
      if (localStorage.getItem('user_id') != null) {
        state.user_id = localStorage.getItem('user_id');
        state.token = localStorage.getItem('token')
        state.name = localStorage.getItem('name')

      }
      else {
        state.user_id = 0;
        state.token = "";
        state.name = ""
      }
    });
    return {
      ...toRefs(state),
      LoginUser,
      logout,
      RegisterUser
    }


  },



}
</script>

<template>
  <header class="pb-3 mb-4 border-bottom">
    <span class="fs-4">
      <nav class="navbar navbar-expand-lg bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" @click="gotoDomain()">Paper Recommend</a>


          <form class="d-flex login-container" v-if="token == ''" @submit.prevent="submitFunc">
            <ul class="nav navbar-nav align-items-center">
              <li class="LiPadding"><input class="form-control me-2" type="text" placeholder="username"
                  aria-label="username" id="username" v-model="account.username"></li>
              <li class="LiPadding"><input class="form-control me-2" type="text" placeholder="Password"
                  aria-label="Password" id="password" v-model="account.password"></li>
              <li class="LiPadding"><button :disabled="account.username === '' | account.password === ''"
                  class="btn btn-outline-success" type="submit" @click="LoginUser()">Login</button></li>

              <li class="LiPadding"><button :disabled="account.username === '' | account.password === ''"
                  class="btn btn-success" type="submit" @click="RegisterUser()">Sign Up</button>
              </li>



            </ul>
          </form>
          <div v-if="token != ''" class="flex ">

            <ul class="nav navbar-nav navbar-right align-items-center">
              <li class="LiPadding"><a class="nav-link disabled">welcome, {{ name }}</a></li>
              <li class="LiPadding"> <a class="nav-link" @click="gotoMyprefer()">My Perference</a></li>
              <li class="LiPadding"><button class="btn btn-outline-warning" type="submit"
                  @click="logout()">Logout</button></li>
            </ul>
          </div>


        </div>
      </nav>
    </span>
  </header>
</template>


<style>
.LiPadding {
  padding: 5px;

}
</style>