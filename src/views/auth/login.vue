<template>
  <div class="form auth-boxed">
    <div class="form-container outer">
      <div class="form-form">
        <div class="form-form-wrap">
          <div class="form-container">
            <div class="form-content">
              <h1 class="">Sign In</h1>
              <p class="">Log in to your account to continue.</p>

              <b-form @submit.prevent="submit" class="text-left">
                <div class="form">
                  <b-form-invalid-feedback class="text-center" :class="{ 'd-block': !valid && form.username && form.password }">Incorrect Username or password</b-form-invalid-feedback>
                  <b-form-invalid-feedback class="text-center" :class="{ 'd-block': is_submit_form1 && !form.username && form.password }">Please fill the username !</b-form-invalid-feedback>
                  <b-form-invalid-feedback class="text-center" :class="{ 'd-block': is_submit_form1 && !form.password && form.username }">Please fill the password !</b-form-invalid-feedback>
                  <b-form-invalid-feedback class="text-center" :class="{ 'd-block': is_submit_form1 && !form.password && !form.username }"
                    >Please fill the username and password !</b-form-invalid-feedback
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
                    <b-input placeholder="e.g John_Doe" v-model="form.username" :class="[is_submit_form1 ? (form.username ? 'is-valid' : 'is-invalid') : '']"></b-input>
                  </div>

                  <div id="password-field" class="field-wrapper input mb-2">
                    <div class="d-flex justify-content-between">
                      <label for="password">PASSWORD</label>
                      <router-link to="/api/password_reset/" class="forgot-pass-link">Forgot Password?</router-link>
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
                    <b-input :type="pwd_type" placeholder="Password" v-model="form.password" :class="[is_submit_form1 ? (form.password ? 'is-valid' : 'is-invalid') : '']"></b-input>
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
                  </div>
                  <div class="d-sm-flex justify-content-between">
                    <div class="field-wrapper">
                      <b-button type="submit" variant="primary" value="">Log In</b-button>
                    </div>
                  </div>
                  <p class="signup-link">Not registered ? <router-link to="/auth/register">Create an account</router-link></p>
                </div>
              </b-form>
              <div class="division">
                <span>OR</span>
              </div>
              <a href="#" class="google-signup mt-2" @click.prevent="loginWithGoogle">
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
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import '@/assets/sass/authentication/auth-boxed.scss';
export default {
  metaInfo: { title: 'Login' },
  data() {
    return {
      pwd_type: 'password',
      form: {
        username: '',
        password: '',
      },
      exist:false,
      valid: true,
      is_submit_form1: false,
    };
  },
  created: function () {
    this.GetUsers();
    this.GetUserprofiles();
    this.GetUserentreprises();
  },
  computed: {
    ...mapGetters({Roles: 'StateRoles',Userentreprises:'StateUserentreprises', Userprofiles: 'StateUserprofiles', Users: 'StateUsers' }),
  },
  methods: {
    ...mapActions(['LogIn','Register','CreateRole','GetUserentreprises', 'GetRoles', 'GetUsers', 'GetUserprofiles']),
    set_pwd_type() {
      if (this.pwd_type == 'password') {
        this.pwd_type = 'text';
      } else {
        this.pwd_type = 'password';
      }
    },
    async submit() {
      
      this.is_submit_form1 = true;
      if (this.form.username && this.form.password) {
        const User = new FormData();
        User.append('username', this.form.username);
        User.append('password', this.form.password);
        try {
          await this.LogIn(User);

          for (let u in this.Users) {
            if (this.Users[u].username == this.form.username) {
              this.CurrentUser = this.Users[u];
              for (let r in this.Roles){
                if(this.CurrentUser.id==this.Roles[r].userRole&& this.CurrentUser.is_superuser){
                  this.exist=true
                }
              }
              if(this.exist==false && this.CurrentUser.is_superuser){
              this.CreateRole({ userRole: this.CurrentUser.id, admin: true });
            }
            
          }}
          let existuserprofile = false;
          for (let uu in this.Userprofiles) {
            if (this.Userprofiles[uu].userU == this.CurrentUser.id) {
              existuserprofile = true;
            }
          }
          let exi=false
          if (existuserprofile == false) {
            
            for(let e in this.Userentreprises){
              if(this.Userentreprises[e].userE==this.CurrentUser.id){
                this.$router.push('/auth/userentrepriseinfo');
                exi=true
              }
            }
            if(exi==false){
              this.$router.push('/auth/userinfo');
            }
            
          } else {
            this.$router.push('/questions');
            this.valid = true;
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
