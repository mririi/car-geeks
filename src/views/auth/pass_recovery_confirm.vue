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
                  <div id="password-field" class="field-wrapper input mb-2">
                    <div class="d-flex justify-content-between">
                      <label for="password">PASSWORD</label>
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
                      class="feather feather-lock"
                    >
                      <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
                      <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                    </svg>
                    <b-input
                      :type="pwd_type"
                      placeholder="Password"
                      v-model="password"
                      :class="[is_submit_form1 ? (password && password.length >= 8 ? 'is-valid' : 'is-invalid') : '']"
                    ></b-input>
                    <svg
                      @click="set_pwd_type"
                      xmlns="http://www.w3.org/2000/svg"
                      width="24"
                      height="24"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      id="toggle-password"
                      class="feather feather-eye"
                    >
                      <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                      <circle cx="12" cy="12" r="3"></circle>
                    </svg>
                    <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !password.length >= 8 }">Please enter a password longer than 8 characters !</b-form-invalid-feedback>
                  </div>

                  <div class="d-sm-flex justify-content-between">
                    <div class="field-wrapper">
                      <b-button v-show="disable" variant="primary" class="disabled">Changing...</b-button>
                      <b-button v-show="!disable" type="submit" variant="primary">Change</b-button>
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
      pwd_type: 'password',
      is_submit_form1: false,
      valid:false,
      disable:false,
    };
  },
  metaInfo: { title: 'Password Recovery Boxed' },
  mounted() {},
  methods: {
    ...mapActions(['SendEmail','GetUsers']),
    set_pwd_type() {
      if (this.pwd_type == 'password') {
        this.pwd_type = 'text';
      } else {
        this.pwd_type = 'password';
      }
    },
    async submit() {
      this.is_submit_form1 = true;
      if (this.password.length>=8) {
        try {
          this.disable=true
      let result=[]
      await axios.post('/api/password_reset/confirm/',{password:this.password,token:this.$route.query.token}).then((res) => {
        result = res.data;
        console.log(res.data)
        if(result.status==="OK")
     {
       this.disable=false
      this.$router.push('/auth/login')
      this.$swal('Password Changed!','Please login with your new password !','success')
     }
      })
    } catch (error) {
          this.disable=false
          this.$swal('Something went wrong!','Your token is expired or Your password is either too commun, entirely numeric or too similar to the username !','error')
        }
    }
    },
  }
};
</script>
