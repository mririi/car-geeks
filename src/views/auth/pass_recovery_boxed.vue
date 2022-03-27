<template>
  <div class="form no-image-content auth-boxed">
    <div class="form-container outer">
      <div class="form-form">
        <div class="form-form-wrap">
          <div class="form-container">
            <div class="form-content">
              <h1 class="">Password Recovery</h1>
              <p class="signup-link recovery">Enter your email and instructions will sent to you!</p>
              <b-form class="text-left" @submit.prevent="sendEmail">
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
                    <b-input type="email" v-model="email" placeholder="Email"></b-input>
                  </div>

                  <div class="d-sm-flex justify-content-between">
                    <div class="field-wrapper">
                      <b-button type="submit" variant="primary">Reset</b-button>
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
//import emailjs from 'emailjs-com';
import '@/assets/sass/authentication/auth-boxed.scss';
export default {
  data() {
    return {
      email: '',
      result:[]
    };
  },
  metaInfo: { title: 'Password Recovery Boxed' },
  mounted() {},
  methods: {

    sendEmail() {

     /* let result=[]
      axios.post('/api/password_reset/',{email:this.email}).then((res) => {
        result = res.data;
        console.log(result)*/

        const options = {
  method: 'POST',
  url: 'https://easymail.p.rapidapi.com/send',
  headers: {
    'content-type': 'application/json',
    'X-RapidAPI-Host': 'easymail.p.rapidapi.com',
    'X-RapidAPI-Key': '82afcb50c4msh7a1e7ea95bac2f4p1d00cfjsn222624a2eea0'
  },
  data: {
    from: {name: 'Firas'},
    to: {name: 'Wassim', address: 'wassim.mriri@gmail.com'},
    subject: 'This is the mail subject',
    message: 'Hello John, how are you ?',
    show_noreply_warning: true
  }
};

axios.request(options).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	console.error(error);
});
        /*
        if(result.status==="OK")
     {
      var templateParams = {
        email: this.email,
        
      };
      emailjs.send('service_mbc13jf', 'template_jo628km', templateParams, 'qI8OZpK-1liHehAv8').then(
        function (response) {
          console.log('SUCCESS!', response.status);
        },
        function (error) {
          console.log('FAILED...', error);
        }
      );
     }
      });*/
   }
  },
};
</script>
