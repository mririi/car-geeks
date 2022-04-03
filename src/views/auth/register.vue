<template>
  <div class="form auth-boxed">
    <div class="form-container outer">
      <div class="form-form">
        <div class="form-form-wrap">
          <div class="form-container">
            <div class="form-content">
              <h1 class="">Register</h1>
              <p class="signup-link register">Already have an account? <router-link to="/auth/login-boxed">Log in</router-link></p>
              <b-form @submit.prevent="submit" class="text-left">
                <div class="form">
                  <b-form-invalid-feedback class="text-center" :class="{ 'd-block': is_submit_form1 && !valid }">Username or email already exists!</b-form-invalid-feedback>
                  <b-form-invalid-feedback class="text-center" :class="{ 'd-block': is_submit_form1 && (!form.password || !form.username || !form.email) }"
                    >Please fill all the fields !</b-form-invalid-feedback
                  >

                  <div id="username-field" class="field-wrapper input">
                    <label for="username">USERNAME</label>
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
                      class="feather feather-user"
                    >
                      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                      <circle cx="12" cy="7" r="4"></circle>
                    </svg>
                    <b-input placeholder="Username" v-model="form.username" :class="[is_submit_form1 ? (form.username && form.username.length >= 8 ? 'is-valid' : 'is-invalid') : '']"></b-input>
                    <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                    <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.username.length >= 8 }">Please enter a username longer than 8 characters !</b-form-invalid-feedback>
                  </div>
                  <div id="email-field" class="field-wrapper input">
                    <label for="email">Email</label>
                    <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 20 20" class="feather feather-lock">
                      <path
                        fill="currentColor"
                        d="M14.608 12.172c0 .84.239 1.175.864 1.175c1.393 0 2.28-1.775 2.28-4.727c0-4.512-3.288-6.672-7.393-6.672c-4.223 0-8.064 2.832-8.064 8.184c0 5.112 3.36 7.896 8.52 7.896c1.752 0 2.928-.192 4.727-.792l.386 1.607c-1.776.577-3.674.744-5.137.744c-6.768 0-10.393-3.72-10.393-9.456c0-5.784 4.201-9.72 9.985-9.72c6.024 0 9.215 3.6 9.215 8.016c0 3.744-1.175 6.6-4.871 6.6c-1.681 0-2.784-.672-2.928-2.161c-.432 1.656-1.584 2.161-3.145 2.161c-2.088 0-3.84-1.609-3.84-4.848c0-3.264 1.537-5.28 4.297-5.28c1.464 0 2.376.576 2.782 1.488l.697-1.272h2.016v7.057h.002zm-2.951-3.168c0-1.319-.985-1.872-1.801-1.872c-.888 0-1.871.719-1.871 2.832c0 1.68.744 2.616 1.871 2.616c.792 0 1.801-.504 1.801-1.896v-1.68z"
                      />
                    </svg>
                    <b-input
                      placeholder="Email@email.com"
                      type="email"
                      v-model="form.email"
                      :class="[is_submit_form1 ? (form.email && email_validate(form.email) ? 'is-valid' : 'is-invalid') : '']"
                    ></b-input>
                    <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                    <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !email_validate(form.email) }">Please fill a correct email !</b-form-invalid-feedback>
                  </div>

                  <div id="password-field" class="field-wrapper input mb-2">
                    <div class="d-flex justify-content-between">
                      <label for="password">PASSWORD</label>
                      <router-link to="/auth/pass-recovery-boxed" class="forgot-pass-link">Forgot Password?</router-link>
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
                      v-model="form.password"
                      :class="[is_submit_form1 ? (form.password && form.password.length >= 8 ? 'is-valid' : 'is-invalid') : '']"
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
                    <b-form-valid-feedback>Looks good!</b-form-valid-feedback>
                    <b-form-invalid-feedback :class="{ 'd-block': is_submit_form1 && !form.password.length >= 8 }">Please enter a password longer than 8 characters !</b-form-invalid-feedback>
                  </div>
                  <b-form-checkbox
                id="checkbox-1"
                v-model="check"
                name="checkbox-1"
                value="1"
                class="text-white mb-3"
              >
               <p>I am an entreprise</p> 
              </b-form-checkbox>
                  <div class="d-sm-flex justify-content-between">
                    <div class="field-wrapper">
                      <b-button type="submit" variant="primary">Get Started!</b-button>
                    </div>
                  </div>
                  <div class="division">
                    <span>OR</span>
                  </div>
                   
                  <div class="social">
                    <a href="#" class="google-signup" @click.prevent="loginWithGoogle">
                      <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18" aria-hidden="true">
                        <title>Google</title>
                        <g fill="none" fill-rule="evenodd">
                          <path
                            fill="#4285F4"
                            d="M17.64 9.2045c0-.6381-.0573-1.2518-.1636-1.8409H9v3.4814h4.8436c-.2086 1.125-.8427 2.0782-1.7959 2.7164v2.2581h2.9087c1.7018-1.5668 2.6836-3.874 2.6836-6.615z"
                          ></path>
                          <path
                            fill="#34A853"
                            d="M9 18c2.43 0 4.4673-.806 5.9564-2.1805l-2.9087-2.2581c-.8059.54-1.8368.859-3.0477.859-2.344 0-4.3282-1.5831-5.036-3.7104H.9574v2.3318C2.4382 15.9832 5.4818 18 9 18z"
                          ></path>
                          <path
                            fill="#FBBC05"
                            d="M3.964 10.71c-.18-.54-.2822-1.1168-.2822-1.71s.1023-1.17.2823-1.71V4.9582H.9573A8.9965 8.9965 0 0 0 0 9c0 1.4523.3477 2.8268.9573 4.0418L3.964 10.71z"
                          ></path>
                          <path
                            fill="#EA4335"
                            d="M9 3.5795c1.3214 0 2.5077.4541 3.4405 1.346l2.5813-2.5814C13.4632.8918 11.426 0 9 0 5.4818 0 2.4382 2.0168.9573 4.9582L3.964 7.29C4.6718 5.1627 6.6559 3.5795 9 3.5795z"
                          ></path>
                        </g>
                      </svg>
                      Google
                    </a>
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
import { mapActions} from 'vuex';
import '@/assets/sass/authentication/auth-boxed.scss';
export default {
  metaInfo: { title: 'Register Boxed' },
  data() {
    return {
      check: null,
      pwd_type: 'password',
      form: {
        username: '',
        email: '',
        password: '',
      },
      valid: true,
      is_submit_form1: false,
    };
  },
  methods: {
    ...mapActions(["CreateRole","isEntreprise",'Register']),
    set_pwd_type() {
      if (this.pwd_type == 'password') {
        this.pwd_type = 'text';
      } else {
        this.pwd_type = 'password';
      }
    },

    email_validate(email) {
      const regexp = /^[\w.%+-]+@[\w.-]+\.[\w]{2,6}$/;
      return regexp.test(email);
    },
    async submit() {
      this.is_submit_form1 = true;
      if (this.form.username && this.form.username.length>=8 && this.form.password.length>=8 && this.form.password && this.form.email) {
        try {
          console.log("wa")
          await this.Register(this.form);
          if (this.check==null){
        await this.isEntreprise(false)
        this.$router.push('/auth/userinfo');
        }else if (this.check==1){
          await this.isEntreprise(true)
          this.$router.push('/auth/userentrepriseinfo');
        }
          
        } catch (error) {
          console.log(error);
          this.valid = false;
        }
      }
    },
    loginWithGoogle() {
      this.$gAuth
        .signIn()
        .then((GoogleUser) => {
          // on success do something
          /*  console.log('GoogleUser', GoogleUser)
          console.log('getId', GoogleUser.getId())
          console.log('basicprofile', GoogleUser.getBasicProfile().getName())
          console.log('getBasicProfile', GoogleUser.getBasicProfile())
          console.log('getAuthResponse', GoogleUser.getAuthResponse())*/
          var userInfo = {
            loginType: 'google',
            google: {
              auth: GoogleUser.getAuthResponse(),
              user: {
                name: GoogleUser.getBasicProfile().getName(),
                email: GoogleUser.getBasicProfile().getEmail(),
                profileImage: GoogleUser.getBasicProfile().getImageUrl(),
                username: GoogleUser.getBasicProfile().getEmail().toLowerCase().slice(0, GoogleUser.getBasicProfile().getEmail().indexOf('@')),
              },
            },
          };
          this.Register({ username: userInfo.google.user.username,email:userInfo.google.user.email,password: 'ggddbxcxw54cwxc5xw4c8s848qc61sc1q9c4dsv1fdbg894nf6bfjf'});
          this.$store.commit('setLoginUser', userInfo);
          this.$router.push('/');
        })
    },
  },
};
</script>
