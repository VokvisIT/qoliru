<template>
    <div class="box loader-2">
        <div class="loader">
            <div class="loader-bar-1"></div>
            <div class="loader-bar-2"></div>
            <div class="loader-bar-3"></div>
        </div>
    </div>
  </template>
  
  <style scoped>
body, html {
  margin: 0;
  padding: 0;
  font-family: "Roboto";
  width: 100%;
  height: 100%;
  background-color: #0C1016;
  font-size: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
}

* {
  box-sizing: border-box;
}

.box {
    display: flex;
    justify-content: center;
}
.loader-2 {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.loader-2 .loader {
  width: 10rem;
  height: 5rem;
  position: relative;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}
.loader-2 .loader div {
  margin: 0 0 1rem 0;
}
.loader-2 .loader .loader-bar-1 {
  width: 5rem;
  height: 0.5rem;
  background-color: #4AD991;
  border-radius: 1rem;
  -webkit-animation: loader-bar-1 1s infinite alternate;
          animation: loader-bar-1 1s infinite alternate;
}
.loader-2 .loader .loader-bar-2 {
  width: 8rem;
  height: 0.5rem;
  background-color: #4AD991;
  border-radius: 1rem;
  -webkit-animation: loader-bar-2 1s infinite alternate;
          animation: loader-bar-2 1s infinite alternate;
}
.loader-2 .loader .loader-bar-3 {
  width: 3rem;
  height: 0.5rem;
  background-color: #4AD991;
  border-radius: 1rem;
  -webkit-animation: loader-bar-3 1s infinite alternate;
          animation: loader-bar-3 1s infinite alternate;
}
@-webkit-keyframes loader-bar-1 {
  0% {
    transform: translateX(-30px);
  }
  100% {
    transform: translateX(30px);
  }
}
@keyframes loader-bar-1 {
  0% {
    transform: translateX(-30px);
  }
  100% {
    transform: translateX(30px);
  }
}
@-webkit-keyframes loader-bar-2 {
  0% {
    transform: translateX(-50px);
  }
  100% {
    transform: translateX(50px);
  }
}
@keyframes loader-bar-2 {
  0% {
    transform: translateX(-50px);
  }
  100% {
    transform: translateX(50px);
  }
}
@-webkit-keyframes loader-bar-3 {
  0% {
    transform: translateX(-60px);
  }
  100% {
    transform: translateX(60px);
  }
}
@keyframes loader-bar-3 {
  0% {
    transform: translateX(-60px);
  }
  100% {
    transform: translateX(60px);
  }
}
  </style>