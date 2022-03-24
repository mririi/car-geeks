<template>
    <div class="layout-px-spacing">
        <portal to="breadcrumb">
            <ul class="navbar-nav flex-row">
                <li>
                    <div class="page-header">
                        <nav class="breadcrumb-one" aria-label="breadcrumb">
                            <ol class="breadcrumb">
                                
                                <li class="breadcrumb-item active" aria-current="page"><span>Contact Us</span></li>
                            </ol>
                        </nav>
                    </div>
                </li>
            </ul>
        </portal>

        <div class="contact-us layout-top-spacing">
          

            <div class="cu-contact-section ">
                
                <div class="contact-form col-lg-12">
                    <perfect-scrollbar tag="form">
                        <div class="cu-section-header">
                            <h4 class="text-center">Contact Us</h4>
                            <p class="text-center">
                                Submit your queries and we will get back
                                to you as soon as possible.
                            </p>
                        </div>

                        <h4>Send us a Message</h4>
                        <div class="row mb-4">
                            <div class="col-sm-12 col-12 input-fields">
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
                                <b-input v-model="form.nameRec"  placeholder="Name"></b-input>
                            </div>
                        </div>
                        <div class="row mb-4">
                            <div class="col-sm-12 col-12 input-fields">
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
                                <b-input type="email" v-model="form.emailRec" placeholder="Email"></b-input>
                            </div>
                        </div>
                        <div class="row mb-4">
                            <div class="col-sm-12 col-12 input-fields">
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
                                    class="feather feather-phone"
                                >
                                    <path
                                        d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"
                                    ></path>
                                </svg>
                                <b-input v-model="form.telRec" placeholder="Phone"></b-input>
                            </div>
                        </div>
                        
                        <div class="row">
                            <div class="col">
                                <div class="form-group input-fields">
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
                                        class="feather feather-mail"
                                    >
                                        <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                                        <polyline points="22,6 12,13 2,6"></polyline>
                                    </svg>
                                    <b-textarea v-model="form.messageRec" placeholder="Message" rows="4"></b-textarea>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col text-sm-left text-center">
                                <b-button type="submit" @click="submit()" class="btn btn-primary mt-4">Submit</b-button>
                            </div>
                        </div>
                    </perfect-scrollbar>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Vue from 'vue';
    import * as VueGoogleMaps from 'vue2-google-maps';
    Vue.use(VueGoogleMaps, {
        load: {
            //key: 'YOUR_API_TOKEN',
            // OR: libraries: 'places,drawing,visualization'
        }
    });

    import '@/assets/sass/pages/contact_us.scss';
    import { mapActions } from 'vuex';
    //import highlight from '@/components/plugins/highlight.vue';
    export default {
        metaInfo: { title: 'Contact Form' },
        components: {
        //    highlight
        },
        data() {
            return {
                form:
                {
                nameRec:'',
                emailRec:'',
                telRec:'',
                messageRec:''
                }
            };
        },
        mounted() {},
        methods: {
             ...mapActions(["CreateReclamation"]),
        async submit(){
            await this.CreateReclamation(this.form)
        this.$swal('We heard you !', 'Your reclamation has been sent successfuly, Wait for our email !', 'success');
        }
        },
    };
</script>
