<template>
    <div class="layout-px-spacing">
        <portal to="breadcrumb">
            <ul class="navbar-nav flex-row">
                <li>
                    <div class="page-header">
                        <nav class="breadcrumb-one" aria-label="breadcrumb">
                            <ol class="breadcrumb">
                                <li class="breadcrumb-item active" aria-current="page"><span>Service Promotions informations</span></li>
                            </ol>
                        </nav>
                    </div>
                </li>
            </ul>
        </portal>
        <div class="coming-soon">
            <div class="coming-soon-container">
                <div class="coming-soon-cont">
                    <div class="coming-soon-wrap">
                        <div class="coming-soon-container">
                            <div class="coming-soon-content">
                                <h4 class="">Coming Soon</h4>
                                <p class="">We will be here in a shortwhile.....</p>

                                <div id="timer">
                                    <div class="days">
                                        <span class="count">{{ days ? days : '--' }}</span> <span class="text">Days</span>
                                    </div>
                                    <div class="hours">
                                        <span class="count">{{ hours ? hours : '--' }}</span> <span class="text">Hours</span>
                                    </div>
                                    <div class="min">
                                        <span class="count">{{ minutes ? minutes : '--' }}</span> <span class="text">Mins</span>
                                    </div>
                                    <div class="sec">
                                        <span class="count">{{ seconds ? seconds : '--' }}</span> <span class="text">Secs</span>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
                <div class="coming-soon-image">
                    <div class="l-image">
                        <div class="img-content">
                            <img src="@/assets/images/mindset.svg" alt="coming_soon" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import '@/assets/sass/pages/coming-soon/style.scss';
    export default {
        metaInfo: { title: 'Comming Soon' },
        data() {
            return {
                days: null,
                hours: null,
                minutes: null,
                seconds: null
            };
        },
        mounted() {
            this.set_timer();
        },
        methods: {
            set_timer() {
                // Set the date we're counting down to
                let getYear = new Date().getFullYear();
                let countDownDate = new Date('Mar 21, ' + getYear + ' 15:37:25').getTime();

                // Update the count down every 1 second
                let countdownfunction = setInterval(() => {
                    // Get todays date and time
                    let now = new Date().getTime();

                    // Find the distance between now an the count down date
                    let distance = countDownDate - now;

                    // Time calculations for days, hours, minutes and seconds
                    this.days = Math.floor(distance / (1000 * 60 * 60 * 24));
                    this.hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                    this.minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                    this.seconds = Math.floor((distance % (1000 * 60)) / 1000);

                    // If the count down is over, write some text
                    if (distance < 0) {
                        clearInterval(countdownfunction);
                        document.getElementById('timer').innerHTML = 'EXPIRED';
                    }
                }, 1000);
            }
        }
    };
</script>
