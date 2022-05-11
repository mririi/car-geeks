import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/index.vue';
import store from '../store';

Vue.use(VueRouter);

const routes = [
    //dashboard
    {
        path: '/',
        name: 'Home',
        component: Home,
        meta: { layout: 'auth' }
    },

    {
        path: '/index2',
        name: 'index2',
        component: () => import(/* webpackChunkName: "index2" */ '../views/index2.vue')
    },

   

    //fonts
    {
        path: '/font-icons',
        name: 'font-icons',
        component: () => import(/* webpackChunkName: "font-icons" */ '../views/font_icons.vue')
    },

    

    //auth
   
    {
        path: '/auth/userinfo',
        name: 'userinfo',
        component: () => import('../views/auth/stepper_userinfo.vue'),
        meta: {
            layout: 'auth',
            requiresAuth: true
        }
    },
    
    
    {
        path: '/api/password_reset/',
        name: 'pass-recovery-boxed',
        component: () => import(/* webpackChunkName: "auth-pass-recovery-boxed" */ '../views/auth/pass_recovery_boxed.vue'),
        meta: { layout: 'auth' }
    },
    {
        path: '/api/password_reset_confirm/',
        query:{token:""},
        name: 'pass-recovery-boxed-confirm',
        component: () => import(/* webpackChunkName: "auth-pass-recovery-boxed" */ '../views/auth/pass_recovery_confirm.vue'),
        meta: { layout: 'auth' }
    },
    //Login
    {
        path: '/auth/login',
        name: 'login',
        component: () => import(/* webpackChunkName: "auth-login" */ '../views/auth/login.vue'),
        meta: { layout: 'auth' }
    },
    //Register
    {
        path: '/auth/register',
        name: 'register',
        component: () => import(/* webpackChunkName: "auth-register" */ '../views/auth/register.vue'),
        meta: { layout: 'auth' }
    },
    //Service Details
    {
        path: '/servicedetails/:id',
        name: 'Service Details',
        component: () => import(/* webpackChunkName: "auth-lockscreen" */ '../views/Services/ServiceDetails.vue'),
        meta: { layout: 'service' }
    },

    //Questions
    {
        path: '/questions',
        name: 'questions',
        component: () => import('../views/Questions/Questions.vue'),
        meta: { layout: 'question' }
    },
    //Add Question
    {
        path: '/addquestion',
        name: 'addquestion',
        component: () => import('../views/Questions/AddQuestion.vue'),
        meta: {
            requiresAuth: true,
        }

    },
    //Update Question
    {
        path: "/updatequestion/:id",
        name: "UpdateQuestion",
        component: () => import('../views/Questions/UpdateQuestion.vue'),
        meta: {
            requiresAuth: true,
            layout: 'question'
        }
    },
    //Question Page(newest)
    {
        path: '/questionpage/:id/:slug',
        name: 'questionpage',
        component: () => import('../views/Questions/QuestionPage.vue'),
        meta: {
            layout: 'question'
        }
    },
    //Question Page(oldest)
    {
        path: '/questionpageoldest/:id/:slug',
        name: 'questionpageoldest',
        component: () => import('../views/Questions/QuestionPage_Oldest.vue'),
        meta: {
            layout: 'question'
        }
    },
    //Question Page(oldest)
    {
        path: '/questionpagemostliked/:id/:slug',
        name: 'questionpagemostliked',
        component: () => import('../views/Questions/QuestionPage_Mostliked.vue'),
        meta: {
            layout: 'question'
        }
    },
    //Question Page(oldest)
    {
        path: '/questionpagerightanswer/:id/:slug',
        name: 'questionpagerightanswer',
        component: () => import('../views/Questions/QuestionPage_Rightanswer.vue'),
        meta: {
            layout: 'question'
        }
    },
    //Services
    {
        path: '/services',
        name: 'services',
        component: () => import('../views/Services/Services.vue'),
        meta: {
            layout: 'service'
        }
    },
    {
        path: '/addservice',
        name: 'addservice',
        component: () => import('../views/Services/AddService.vue'),
        meta: {
            requiresAuth: true,
        }
    },
    {
        path: '/updateservice/:id',
        name: 'updateservice',
        component: () => import('../views/Services/UpdateService.vue'),
        meta: {
            layout: 'service',
            requiresAuth: true,
        }
    },
    {
        path: '/promoinfo',
        name: 'promoinfo',
        component: () => import('../views/Services/PromoInfo.vue'),
        meta: {
            layout: 'service',
            requiresAuth: true,
        }
    },
    //Entreprises
    {
        path: '/entreprises',
        name: 'entreprises',
        component: () => import('../views/Entreprises/Entreprises.vue'),
        meta: {
            layout: 'app'
        }
    },
    {
        path: '/entreprisedetails/:id',
        name: 'entreprisedetails',
        component: () => import('../views/Entreprises/EntrepriseDetails.vue'),
        meta: {
            layout: 'app'
        }
    },
    {
        path: '/auth/userentrepriseinfo',
        name: 'userentreprise',
        component: () => import('../views/auth/stepper_userentrepriseinfo.vue'),
        meta: {
            layout: 'auth'
        }
    },
    {
        path: '/updateentreprise/:id',
        name: 'userentrepriseupdate',
        component: () => import('../views/Entreprises/UpdateEntreprise.vue'),
        meta: {
            layout: 'app'
        }
    },
    {
        path: '/promoinfoentreprise/:id',
        name: 'userentreprisepromoinfo',
        component: () => import('../views/Entreprises/PromoInfoEntreprise.vue'),
        meta: {
            layout: 'app'
        }
    },
    //News
    {
        path: '/news',
        name: 'news',
        component: () => import('../views/Others/News.vue'),
        meta: {
            layout: 'app'
        }
    },
    //Faq
    {
        path: '/faq',
        name: 'faq',
        component: () => import('../views/Others/faq.vue'),
        meta: {
            layout: 'app'
        }
    },
    //Contact-us
    {
        path: '/contact-us',
        name: 'contactus',
        component: () => import('../views/Others/contact_us.vue'),
        meta: {
            layout: 'app'
        }
    },
    //Groups
    {
        path: '/groups',
        name: 'groups',
        component: () => import('../views/Groups/Groups.vue'),
        meta: {
            layout: 'group'
        }
    },
    //Group Details
    {
        path: '/groupdetail/:id',
        name: 'groupdetail',
        component: () => import('../views/Groups/GroupDetails.vue'),
        meta: {
            layout: 'app'
        }
    },
    //Create Group
    {
        path: '/creategroup',
        name: 'creategroup',
        component: () => import('../views/Groups/CreateGroup.vue'),
        meta: {
            layout: 'app'
        }
    },
     //Add Post Group
     {
        path: '/group/:id/addpost/',
        name: 'addpost',
        component: () => import('../views/Groups/AddPost.vue'),
        meta: {
            layout: 'app'
        }
    },
     //Update Post Group
     {
        path: '/group/:id/updatepost/:id',
        name: 'updatepost',
        component: () => import('../views/Groups/UpdatePost.vue'),
        meta: {
            layout: 'app'
        }
    },
    //Dashboard
    {
        path: '/dashboard',
        name: 'dashboard',
        component: () => import('../views/Admin/Dashboard.vue'),
        meta: {
            layout: 'dashboard'
        }
    },
    //Reclamations Dashboard
    {
        path: '/dashboard/reclamations',
        name: 'reclamations',
        component: () => import('../views/Admin/Reclamations.vue'),
        meta: {
            layout: 'dashboard'
        }
    },
       //Users
    {
        path: "/dashboard/users",
        name: 'users',
        component: () => import('../views/Admin/Users.vue'),
        meta: {
            layout: 'dashboard'
        },
    },

     //Questions Dashboard
     {
        path: "/dashboard/questionlist",
        name: 'questionlist',
        component: () => import('../views/Admin/QuestionList.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
     //Question Category Dashboard
     {
        path: "/dashboard/categorylist",
        name: 'categorylist',
        component: () => import('../views/Admin/QuestionCategoryList.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
     //Service Types Dashboard
     {
        path: "/dashboard/typeslist",
        name: 'typeslist',
        component: () => import('../views/Admin/ServiceTypesList.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //User service verfication Dashboard
    {
        path: "/dashboard/userverifications",
        name: 'userverifications',
        component: () => import('../views/Admin/UserserviceVerification.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //User service verfication Dashboard
    {
        path: "/dashboard/userverificationrequest",
        name: 'userverificationrequest',
        component: () => import('../views/Admin/UserserviceVerificationRequests.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
     //Add Category Dashboard
     {
        path: "/dashboard/addcategory",
        name: 'addcategory',
        component: () => import('../views/Admin/AddQuestionCategory.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
     //Add Type Dashboard
     {
        path: "/dashboard/addtype",
        name: 'addtype',
        component: () => import('../views/Admin/AddServiceType.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Questions Requests
    {
        path: "/dashboard/questionrequests",
        name: 'questionrequests',
        component: () => import('../views/Admin/QuestionRequests.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
     //Replies Dashboard
     {
        path: "/dashboard/replieslist",
        name: 'replieslist',
        component: () => import('../views/Admin/RepliesList.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Replies Requests
    {
        path: "/dashboard/repliesrequests",
        name: 'repliesrequests',
        component: () => import('../views/Admin/RepliesRequests.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Comments dashboard
    {
        path: "/dashboard/commentslist",
        name: 'commentslist',
        component: () => import('../views/Admin/CommentList.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Services dashboard
    {
        path: "/dashboard/servicelist",
        name: 'servicelist',
        component: () => import('../views/Admin/ServiceList.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Services Requests
    {
        path: "/dashboard/servicerequests",
        name: 'servicerequests',
        component: () => import('../views/Admin/ServiceRequests.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Entreprises Dashboard
    {
        path: "/dashboard/entrepriselist",
        name: 'entrepriselist',
        component: () => import('../views/Admin/EntreprisesList.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Entreprises Requests
    {
        path: "/dashboard/entrepriserequests",
        name: 'entrepriserequests',
        component: () => import('../views/Admin/EntrepriseRequests.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Promoted Services Dashboard
    {
        path: "/dashboard/promotedservices",
        name: 'promotedservices',
        component: () => import('../views/Admin/PromotedServices.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Promotion Services Requests
    {
        path: "/dashboard/promotionservicerequests",
        name: 'promotionservicerequests',
        component: () => import('../views/Admin/PromotionServiceRequests.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Promoted Entreprises Dashboard
    {
        path: "/dashboard/promotedentreprises",
        name: 'promotedentreprises',
        component: () => import('../views/Admin/PromotedEntreprises.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Promotion Entreprises Requests
    {
        path: "/dashboard/promotionentrepriserequests",
        name: 'promotionentrepriserequests',
        component: () => import('../views/Admin/PromotionEntrepriseRequests.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Group List Dashboard
    {
        path: "/dashboard/grouplist",
        name: 'grouplist',
        component: () => import('../views/Admin/GroupList.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    //Group Requests Dashboard
    {
        path: "/dashboard/grouprequests",
        name: 'grouprequests',
        component: () => import('../views/Admin/GroupRequests.vue'),
        meta: {
            layout: 'dashboard'
        },
    },
    

    //Group Dashboard
    {
        path: "/groupdashboard/:id/dashboard",
        name: 'groupdashboard',
        component: () => import('../views/Group Admin/Dashboard.vue'),
        meta: {
            layout: 'groupdashboard'
        },
    },
    //Group Dashboard Users
    {
        path: "/groupdashboard/:id/users",
        name: 'groupdashboardusers',
        component: () => import('../views/Group Admin/Users.vue'),
        meta: {
            layout: 'groupdashboard'
        },
    },
    //Group Dashboard Entreprises
    {
        path: "/groupdashboard/:id/entreprises",
        name: 'groupdashboardentreprises',
        component: () => import('../views/Group Admin/Entreprises.vue'),
        meta: {
            layout: 'groupdashboard'
        },
    },
    //Group Dashboard Join requests
    {
        path: "/groupdashboard/:id/join",
        name: 'groupdashboardjoin',
        component: () => import('../views/Group Admin/JoinRequests.vue'),
        meta: {
            layout: 'groupdashboard'
        },
    },
     //Group Dashboard Entreprise Join requests
     {
        path: "/groupdashboard/:id/entreprisejoin",
        name: 'groupdashboardentreprisejoin',
        component: () => import('../views/Group Admin/EntrepriseRequests.vue'),
        meta: {
            layout: 'groupdashboard'
        },
    },
    //Group Dashboard Posts List
    {
        path: "/groupdashboard/:id/postslist",
        name: 'groupdashboardpostslist',
        component: () => import('../views/Group Admin/PostsList.vue'),
        meta: {
            layout: 'groupdashboard'
        },
    },
    //Group Dashboard PostRequests
    {
        path: "/groupdashboard/:id/postrequests",
        name: 'groupdashboardpostrequests',
        component: () => import('../views/Group Admin/PostRequests.vue'),
        meta: {
            layout: 'groupdashboard'
        },
    },

    

   
    //users
    {
        path: '/profile/:id',
        name: 'profile',
        component: () => import(/* webpackChunkName: "users-profile" */ '../views/users/profile.vue')
    },
    {
        path: '/profile-edit/:id',
        name: 'account-setting',
        component: () => import(/* webpackChunkName: "users-account-setting" */ '../views/users/account_setting.vue')
    },

    //drag&drop
    {
        path: '/dragndrop',
        name: 'dragndrop',
        component: () => import(/* webpackChunkName: "dragndrop" */ '../views/dragndrop.vue')
    },

    //charts
    {
        path: '/charts/apex-chart',
        name: 'apex-chart',
        component: () => import(/* webpackChunkName: "charts-apex-chart" */ '../views/charts/apex_chart.vue')
    },


    //apps
    {
        path: '/apps/chat',
        name: 'chat',
        component: () => import(/* webpackChunkName: "apps-chat" */ '../views/apps/chat.vue')
    },
   
];

const router = new VueRouter({
    mode: 'history',
    linkExactActiveClass: 'active',
    routes,
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition;
        } else {
            return { x: 0, y: 0 };
        }
    }
});

router.beforeEach((to, from, next) => {
    if (to.meta && to.meta.layout && to.meta.layout == 'auth') {
        store.commit('setLayout', 'auth');
    } else if (to.meta && to.meta.layout && to.meta.layout == 'question') {
        store.commit('setLayout', 'question');
    } else if (to.meta && to.meta.layout && to.meta.layout == 'service') {
        store.commit('setLayout', 'service');
    } else if (to.meta && to.meta.layout && to.meta.layout == 'dashboard') {
        store.commit('setLayout', 'dashboard');
    } else if (to.meta && to.meta.layout && to.meta.layout == 'group') {
        store.commit('setLayout', 'group');
    } else if (to.meta && to.meta.layout && to.meta.layout == 'groupdashboard') {
        store.commit('setLayout', 'groupdashboard');
    } else {
        store.commit('setLayout', 'app');
    }
    next(true);
});
router.beforeEach((to, from, next) => {
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (store.getters.isAuthenticated) {
            next();
            return;
        }
        next("/auth/login");
    } else {
        next();
    }
});

export default router;
