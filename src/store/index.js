import Vue from 'vue';
import Vuex from 'vuex';
import i18n from '../i18n';
import axios from 'axios'
Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        layout: 'app',
        is_show_sidebar: true,
        is_show_search: false,
        is_dark_mode: false,
        dark_mode: 'light',
        locale: null,
        menu_style: 'vertical',
        layout_style: 'full',
        countryList: [
            { code: 'zh', name: 'Chinese' },
            { code: 'da', name: 'Danish' },
            { code: 'en', name: 'English' },
            { code: 'fr', name: 'French' },
            { code: 'de', name: 'German' },
            { code: 'el', name: 'Greek' },
            { code: 'hu', name: 'Hungarian' },
            { code: 'it', name: 'Italian' },
            { code: 'ja', name: 'Japanese' },
            { code: 'pl', name: 'Polish' },
            { code: 'pt', name: 'Portuguese' },
            { code: 'ru', name: 'Russian' },
            { code: 'es', name: 'Spanish' },
            { code: 'sv', name: 'Swedish' },
            { code: 'tr', name: 'Turkish' }
        ],
        user: null,
        users:null,
        //QUESTION
        questions: null,
    },
    mutations: {
        setLayout(state, payload) {
            state.layout = payload;
        },
        toggleSideBar(state, value) {
            state.is_show_sidebar = value;
        },
        toggleSearch(state, value) {
            state.is_show_search = value;
        },
        toggleLocale(state, value) {
            value = value || 'en';
            i18n.locale = value;
            localStorage.setItem('i18n_locale', value);
            state.locale = value;
        },

        toggleDarkMode(state, value) {
            //light|dark|system
            value = value || 'light';
            localStorage.setItem('dark_mode', value);
            state.dark_mode = value;
            if (value == 'light') {
                state.is_dark_mode = false;
            } else if (value == 'dark') {
                state.is_dark_mode = true;
            } else if (value == 'system') {
                if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                    state.is_dark_mode = true;
                } else {
                    state.is_dark_mode = false;
                }
            }

            if (state.is_dark_mode) {
                document.querySelector('body').classList.add('dark');
            } else {
                document.querySelector('body').classList.remove('dark');
            }
        },

        toggleMenuStyle(state, value) {
            //horizontal|vertical|collapsible-vertical
            value = value || '';
            localStorage.setItem('menu_style', value);
            state.menu_style = value;
            if (!value || value === 'vertical') {
                state.is_show_sidebar = true;
            } else if (value === 'collapsible-vertical') {
                state.is_show_sidebar = false;
            }
        },

        toggleLayoutStyle(state, value) {
            //boxed-layout|large-boxed-layout|full
            value = value || '';
            localStorage.setItem('layout_style', value);
            state.layout_style = value;
        },
        setUser(state, username) {
            state.user = username;
          },
          setUsers(state, users) {
            state.users = users;
          },
        //QUESTION
        setQuestions(state, questions) {
            state.questions = questions;
        },
    },
    getters: {
        layout(state) {
            return state.layout;
        },
        isAuthenticated: (state) => !!state.user,
        StateUser: (state) => state.user,
        StateRoles: (state) => state.roles,
        StateUsers: (state) => state.users,
        //QUESTION
        StateQuestions: (state) => state.questions,
    },
    actions: {
        async Register({dispatch}, form) {
            await axios.post('user/users/', form)
            let UserForm = new FormData()
            UserForm.append('username', form.username)
            UserForm.append('password', form.password)
            await dispatch('LogIn', UserForm)
          },
          async LogIn({commit}, user) {
            await axios.post("/auth/", user);
            await commit("setUser", user.get("username"));
          },
          async LogOut({ commit }) {
            let user = null;
            commit("logout", user);
          },
          async GetQuestions({ commit }) {
            let response = await axios.get("question/question-list/");
            commit("setQuestions", response.data);
          },
    },
    modules: {}
});