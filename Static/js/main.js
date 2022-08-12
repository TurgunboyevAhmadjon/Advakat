//const modal_btn = document.querySelector(".menu-icon");
//const exit = document.querySelector(".exit");
//const modal = document.querySelector(".modal");
//
//modal_btn.addEventListener("click", ()=>{
//    modal.classList.add("active")
//})
//exit.addEventListener("click", () => {
//      modal.classList.remove("active");
//});

// accardion

// const accardion_title = document.querySelector(".accardion-title");
// const accardion_info = document.querySelector(".accardion-info");
// const plus = document.querySelector(".plus");
// const minus = document.querySelector(".minus");

// accardion_title.addEventListener("click", ()=>{
//     accardion_info.classList.toggle("active")
//     accardion_title.classList.toggle("active");
//     plus.classList.toggle("active")
//     minus.classList.toggle("active");
// })



//document.addEventListener("click", (e) => {
//    const accardion_info =e.target.parentElement.querySelector(".accardion-info");
//    const plus = e.target.parentElement.querySelector(".plus");
//    const minus = e.target.parentElement.querySelector(".minus");
//  if (e.target.classList.value == "accardion-title") {
//    e.target.classList.add("active");
//    accardion_info.classList.add("active");
//    plus.classList.add("active");
//    minus.classList.add("active");
//  }else{
//    e.target.classList.remove("active");
//    accardion_info.classList.remove("active");
//    plus.classList.remove("active");
//    minus.classList.remove("active");
//  }
//});




const modal_btn = document.querySelector(".menu-icon");
const exit = document.querySelector(".exit");
const modal = document.querySelector(".modal");

modal_btn.addEventListener("click", ()=>{
    modal.classList.add("active")
})
exit.addEventListener("click", () => {
      modal.classList.remove("active");
});



document.addEventListener("click", (e) => {
    const accardion_info =e.target.parentElement.querySelector(".accardion-info");
    const plus = e.target.parentElement.querySelector(".plus");
    const minus = e.target.parentElement.querySelector(".minus");
  if (e.target.classList.value == "accardion-title") {
    e.target.classList.add("active");
    accardion_info.classList.add("active");
    plus.classList.add("active");
    minus.classList.add("active");
  }else{
    e.target.classList.remove("active");
    accardion_info.classList.remove("active");
    plus.classList.remove("active");
    minus.classList.remove("active");
  }
});
const exit_login = document.querySelector(".exit-login");
const login = document.querySelector(".login");
const login_page = document.querySelector(".login-page");

login.addEventListener("click", () => {
  login_page.classList.add("login-click");
});

exit_login.addEventListener("click", ()=>{
  login_page.classList.remove("login-click");
})