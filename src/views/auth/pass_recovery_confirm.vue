<template>
  <div class="form no-image-content auth-boxed">
    <div class="form-container outer">
      <div class="form-form">
        <div class="form-form-wrap">
          <div class="form-container">
            <div class="form-content">
              <h1 class="">Password Recovery Confirmation</h1>
              <p class="signup-link recovery">Enter your New Password !</p>
              <b-form class="text-left" @submit.prevent="submit">
                <div class="form">
                  <div id="email-field" class="field-wrapper input">
                    <div class="d-flex justify-content-between">
                      <label for="email">EMAIL</label>
                    </div>
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="24"
                      height="24"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      class="feather feather-at-sign"
                    >
                      <circle cx="12" cy="12" r="4"></circle>
                      <path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-3.92 7.94"></path>
                    </svg>
                    <b-input type="password" v-model="password" placeholder="Password"></b-input>
                  </div>

                  <div class="d-sm-flex justify-content-between">
                    <div class="field-wrapper">
                      <b-button type="submit" variant="primary">Change</b-button>
                    </div>
                  </div>
                </div>
              </b-form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex';
import '@/assets/sass/authentication/auth-boxed.scss';
export default {
  data() {
    return {
      password: '',
      result:[],
    };
  },
  metaInfo: { title: 'Password Recovery Boxed' },
  mounted() {},
  methods: {
    ...mapActions(['SendEmail','GetUsers']),
    submit() {
      let result=[]
      axios.post('/api/password_reset/confirm/',{password:this.password,token:this.$route.query.token}).then((res) => {
        result = res.data;
        console.log(result)
        if(result.status==="OK")
     {
      this.$router.push('/login')
      this.$swal('Password Changed!','Please login with your new password !','success')
     }
      })
    }},
    created(){
      console.log(this.$route.query.token)
    }
   
};
</script>
