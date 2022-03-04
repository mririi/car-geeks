<template>
    <!--  BEGIN SIDEBAR  -->
    <div class="sidebar-wrapper float-right sidebar-theme ">
        <nav ref="menu" id="sidebar">
            <div class="shadow-bottom"></div>

            <perfect-scrollbar class="list-unstyled menu-categories" tag="ul" :options="{ wheelSpeed: 0.5, swipeEasing: !0, minScrollbarLength: 40, maxScrollbarLength: 300, suppressScrollX: true }">
                <router-link tag="li" to="/" class="menu" @click.native="toggleMobileMenu">
                    <a class="dropdown-toggle">
                        <div class="">
                            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 20 20"><path fill="currentColor" d="m16 8.5l1.53 1.53l-1.06 1.06L10 4.62l-6.47 6.47l-1.06-1.06L10 2.5l4 4v-2h2v4zm-6-2.46l6 5.99V18H4v-5.97zM12 17v-5H8v5h4z"/></svg>
                            <span>{{ $t('Home') }}</span>
                        </div>
                    </a>
                </router-link>
                <router-link tag="li" to="/questions" class="menu" @click.native="toggleMobileMenu">
                    <a class="dropdown-toggle">
                        <div class="">
                            <svg xmlns="http://www.w3.org/2000/svg" 
                            aria-hidden="true" 
                            role="img" 
                            width="1em" 
                            height="1em" 
                            preserveAspectRatio="xMidYMid meet" 
                            viewBox="0 0 512 512">
                            <path fill="currentColor" d="M504 256c0 136.997-111.043 248-248 248S8 392.997 8 256C8 119.083 119.043 8 256 8s248 111.083 248 248zM262.655 90c-54.497 0-89.255 22.957-116.549 63.758c-3.536 5.286-2.353 12.415 2.715 16.258l34.699 26.31c5.205 3.947 12.621 3.008 16.665-2.122c17.864-22.658 30.113-35.797 57.303-35.797c20.429 0 45.698 13.148 45.698 32.958c0 14.976-12.363 22.667-32.534 33.976C247.128 238.528 216 254.941 216 296v4c0 6.627 5.373 12 12 12h56c6.627 0 12-5.373 12-12v-1.333c0-28.462 83.186-29.647 83.186-106.667c0-58.002-60.165-102-116.531-102zM256 338c-25.365 0-46 20.635-46 46c0 25.364 20.635 46 46 46s46-20.636 46-46c0-25.365-20.635-46-46-46z"/>
                        </svg>
                            <span>{{ $t('Questions') }}</span>
                        </div>
                    </a>
                </router-link>
                <router-link tag="li" to="/services" class="menu" @click.native="toggleMobileMenu">
                    <a class="dropdown-toggle">
                        <div class="">
                            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 512 512"><path fill="currentColor" d="M501.1 395.7L384 278.6c-23.1-23.1-57.6-27.6-85.4-13.9L192 158.1V96L64 0L0 64l96 128h62.1l106.6 106.6c-13.6 27.8-9.2 62.3 13.9 85.4l117.1 117.1c14.6 14.6 38.2 14.6 52.7 0l52.7-52.7c14.5-14.6 14.5-38.2 0-52.7zM331.7 225c28.3 0 54.9 11 74.9 31l19.4 19.4c15.8-6.9 30.8-16.5 43.8-29.5c37.1-37.1 49.7-89.3 37.9-136.7c-2.2-9-13.5-12.1-20.1-5.5l-74.4 74.4l-67.9-11.3L334 98.9l74.4-74.4c6.6-6.6 3.4-17.9-5.7-20.2c-47.4-11.7-99.6.9-136.6 37.9c-28.5 28.5-41.9 66.1-41.2 103.6l82.1 82.1c8.1-1.9 16.5-2.9 24.7-2.9zm-103.9 82l-56.7-56.7L18.7 402.8c-25 25-25 65.5 0 90.5s65.5 25 90.5 0l123.6-123.6c-7.6-19.9-9.9-41.6-5-62.7zM64 472c-13.2 0-24-10.8-24-24c0-13.3 10.7-24 24-24s24 10.7 24 24c0 13.2-10.7 24-24 24z"/></svg>
                            <span>{{ $t('Services') }}</span>
                        </div>
                    </a>
                </router-link>
                <router-link tag="li" to="/entreprises" class="menu" @click.native="toggleMobileMenu">
                    <a class="dropdown-toggle">
                        <div class="">
                            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="0.88em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 448 512"><path fill="currentColor" d="M436 480h-20V24c0-13.255-10.745-24-24-24H56C42.745 0 32 10.745 32 24v456H12c-6.627 0-12 5.373-12 12v20h448v-20c0-6.627-5.373-12-12-12zM128 76c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v40c0 6.627-5.373 12-12 12h-40c-6.627 0-12-5.373-12-12V76zm0 96c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v40c0 6.627-5.373 12-12 12h-40c-6.627 0-12-5.373-12-12v-40zm52 148h-40c-6.627 0-12-5.373-12-12v-40c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v40c0 6.627-5.373 12-12 12zm76 160h-64v-84c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v84zm64-172c0 6.627-5.373 12-12 12h-40c-6.627 0-12-5.373-12-12v-40c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v40zm0-96c0 6.627-5.373 12-12 12h-40c-6.627 0-12-5.373-12-12v-40c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v40zm0-96c0 6.627-5.373 12-12 12h-40c-6.627 0-12-5.373-12-12V76c0-6.627 5.373-12 12-12h40c6.627 0 12 5.373 12 12v40z"/></svg>
                            <span>{{ $t('Entreprises') }}</span>
                        </div>
                    </a>
                </router-link>
                <router-link tag="li" to="/groups" class="menu" @click.native="toggleMobileMenu">
                    <a class="dropdown-toggle">
                        <div class="">
                            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 36 36"><path fill="currentColor" d="M12 16.14h-.87a8.67 8.67 0 0 0-6.43 2.52l-.24.28v8.28h4.08v-4.7l.55-.62l.25-.29a11 11 0 0 1 4.71-2.86A6.59 6.59 0 0 1 12 16.14Z" class="clr-i-solid clr-i-solid-path-1"/><path fill="currentColor" d="M31.34 18.63a8.67 8.67 0 0 0-6.43-2.52a10.47 10.47 0 0 0-1.09.06a6.59 6.59 0 0 1-2 2.45a10.91 10.91 0 0 1 5 3l.25.28l.54.62v4.71h3.94v-8.32Z" class="clr-i-solid clr-i-solid-path-2"/><path fill="currentColor" d="M11.1 14.19h.31a6.45 6.45 0 0 1 3.11-6.29a4.09 4.09 0 1 0-3.42 6.33Z" class="clr-i-solid clr-i-solid-path-3"/><path fill="currentColor" d="M24.43 13.44a6.54 6.54 0 0 1 0 .69a4.09 4.09 0 0 0 .58.05h.19A4.09 4.09 0 1 0 21.47 8a6.53 6.53 0 0 1 2.96 5.44Z" class="clr-i-solid clr-i-solid-path-4"/><circle cx="17.87" cy="13.45" r="4.47" fill="currentColor" class="clr-i-solid clr-i-solid-path-5"/><path fill="currentColor" d="M18.11 20.3A9.69 9.69 0 0 0 11 23l-.25.28v6.33a1.57 1.57 0 0 0 1.6 1.54h11.49a1.57 1.57 0 0 0 1.6-1.54V23.3l-.24-.3a9.58 9.58 0 0 0-7.09-2.7Z" class="clr-i-solid clr-i-solid-path-6"/><path fill="none" d="M0 0h36v36H0z"/></svg>
                            <span>{{ $t('Groups') }}</span>
                        </div>
                    </a>
                </router-link>
                <router-link tag="li" to="/news" class="menu" @click.native="toggleMobileMenu">
                    <a class="dropdown-toggle">
                        <div class="">
                            <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1.13em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 576 512"><path fill="currentColor" d="M552 64H88c-13.255 0-24 10.745-24 24v8H24c-13.255 0-24 10.745-24 24v272c0 30.928 25.072 56 56 56h472c26.51 0 48-21.49 48-48V88c0-13.255-10.745-24-24-24zM56 400a8 8 0 0 1-8-8V144h16v248a8 8 0 0 1-8 8zm236-16H140c-6.627 0-12-5.373-12-12v-8c0-6.627 5.373-12 12-12h152c6.627 0 12 5.373 12 12v8c0 6.627-5.373 12-12 12zm208 0H348c-6.627 0-12-5.373-12-12v-8c0-6.627 5.373-12 12-12h152c6.627 0 12 5.373 12 12v8c0 6.627-5.373 12-12 12zm-208-96H140c-6.627 0-12-5.373-12-12v-8c0-6.627 5.373-12 12-12h152c6.627 0 12 5.373 12 12v8c0 6.627-5.373 12-12 12zm208 0H348c-6.627 0-12-5.373-12-12v-8c0-6.627 5.373-12 12-12h152c6.627 0 12 5.373 12 12v8c0 6.627-5.373 12-12 12zm0-96H140c-6.627 0-12-5.373-12-12v-40c0-6.627 5.373-12 12-12h360c6.627 0 12 5.373 12 12v40c0 6.627-5.373 12-12 12z"/></svg>
                            <span>{{ $t('News') }}</span>
                        </div>
                    </a>
                </router-link>
                <router-link tag="li" to="/contactus" class="menu" @click.native="toggleMobileMenu">
                    <a class="dropdown-toggle">
                        
                        <div class="">
                           <svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 1536 1536"><path fill="currentColor" d="M515 783v128H263V783h252zm0-255v127H263V528h252zm758 511v128H932v-128h341zm0-256v128H601V783h672zm0-255v127H601V528h672zm135 860V148q0-8-6-14t-14-6h-32L978 384L768 213L558 384L180 128h-32q-8 0-14 6t-6 14v1240q0 8 6 14t14 6h1240q8 0 14-6t6-14zM553 278l185-150H332zm430 0l221-150H798zm553-130v1240q0 62-43 105t-105 43H148q-62 0-105-43T0 1388V148Q0 86 43 43T148 0h1240q62 0 105 43t43 105z"/></svg>
                            <span>{{ $t('Contact-us') }}</span>
                        </div>
                    </a>
                </router-link>
                <!--</ul>-->
            </perfect-scrollbar>
        </nav>
    </div>
    <!--  END SIDEBAR  -->
</template>
<script>
    export default {
        data() {
            return { menu_collapse: 'dashboard' };
        },

        watch: {
            $route(to) {
                const selector = document.querySelector('#sidebar a[href="' + to.path + '"]');
                const ul = selector.closest('ul.collapse');
                if (!ul) {
                    const ele = document.querySelector('.dropdown-toggle.not-collapsed');
                    if (ele) {
                        ele.click();
                    }
                }
            }
        },

        mounted() {
            // default menu selection on refresh
            const selector = document.querySelector('#sidebar a[href="' + window.location.pathname + '"]');
            if (selector) {
                const ul = selector.closest('ul.collapse');
                if (ul) {
                    let ele = ul.closest('li.menu').querySelectorAll('.dropdown-toggle');
                    if (ele) {
                        ele = ele[0];
                        setTimeout(() => {
                            ele.click();
                        });
                    }
                } else {
                    selector.click();
                }
            }
        },

        methods: {
            toggleMobileMenu() {
                if (window.innerWidth < 991) {
                    this.$store.commit('toggleSideBar', !this.$store.state.is_show_sidebar);
                }
            }
        }
    };
</script>
