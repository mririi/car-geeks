<template>
  <div class="form no-image-content auth-boxed">
    <div class="form-container outer">
      <div class="form-form">
        <div class="form-form-wrap">
          <div class="form-container">
            <div class="form-content">
              <h1 class="">Password Recovery</h1>
              <p class="signup-link recovery">Enter your email and instructions will sent to you!</p>
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
                    <b-input type="email"
                     :class="[is_submit_form1 ? (email && email_validate(email) ? 'is-valid' : 'is-invalid') : '']"
                     v-model="email" placeholder="Email"></b-input>
                  <b-form-valid-feedback>Form looks good!</b-form-valid-feedback>
                    <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !email_validate(email) }">Please fill a correct email !</b-form-invalid-feedback>
                 
                  </div>

                  <div class="d-sm-flex justify-content-between">
                    <div class="field-wrapper">
                      <b-button v-show="disable" variant="primary" class="disabled">Sending the email</b-button>
                      <b-button v-show="!disable" type="submit" variant="primary">Reset</b-button>
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
      email: '',
      result:[],
      disable:false,
      is_submit_form1:false,
    };
  },
  metaInfo: { title: 'Password Recovery' },
  mounted() {},
  methods: {
    ...mapActions(['SendEmail']),
    email_validate(email) {
      const regexp = /^[\w.%+-]+@[\w.-]+\.[\w]{2,6}$/;
      return regexp.test(email);
    },
    async submit() {
      this.is_submit_form1 = true;
      if (this.email) {
      try{
      this.disable=true
      let result=[]
      await axios.post('/api/password_reset/',{email:this.email}).then((res) => {
        result = res.data;
        if(result.status==="OK")
     {
      this.disable=false
      this.$swal('Email Sent!','Please check your email !','success')
     }
      })}catch(error){
        this.disable=false
        this.$swal('Something went wrong!','This email does not exist in our database !','error')
      }}
    }}
   
};
</script>
