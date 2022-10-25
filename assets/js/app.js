var numberSpinner = (function() {
    $('.number-spinner>.ns-btn>a').click(function() {
      var btn = $(this),
        oldValue = btn.closest('.number-spinner').find('input').val().trim(),
        newVal = 0;
  
      if (btn.attr('data-dir') === 'up') {
        newVal = parseInt(oldValue) + 1;
      } else {
        if (oldValue > 0) {
          newVal = parseInt(oldValue) - 1;
        } else {
          newVal = 0;
        }
      }
      btn.closest('.number-spinner').find('input').val(newVal);
    });
    $('.number-spinner>input').keypress(function(evt) {
      evt = (evt) ? evt : window.event;
      var charCode = (evt.which) ? evt.which : evt.keyCode;
      if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
      }
      return true;
    });
  })();
  var kitablar = [{
      id:1,
      src:"../assets/images/inkognito.png",
      bookname:"Meditations",
      outhor:"viktor huqo",
      class:"psixalogiya"},
  {
    id:2,
    src:"../assets/images/inkognito.png",
    bookname:"Meditations",
    outhor:"viktor huqo",
    class:"roman"},
    {
    id:3,
    src:"../assets/images/inkognito.png",
    bookname:"Meditations",
    outhor:"viktor huqo",
    class:"roman"},
        {
    id:4,
    src:"../assets/images/inkognito.png",
    bookname:"Meditations",
    outhor:"viktor huqo",
    class:"roman"},
            {
    id:5,
    src:"../assets/images/inkognito.png",
    bookname:"Meditations",
    outhor:"viktor huqo",
    class:"bilim-kurgu"}

]
var choosenbook=[]


$(".up").click( () =>{
    var random=Math.floor(Math.random() * kitablar.length)
    var condition=true;
    while (condition){
        if (choosenbook.includes(random) && choosenbook.length<6){
            random=Math.floor(Math.random() * kitablar.length)
        }
        else if (choosenbook.length==6){
            condition= false;

        }
        else{
            choosenbook.push(random)
    
       var add= `<div id="${kitablar[random].id}" class="col-4 d-flex justify-content-center grid-item ${kitablar[random].class} "><div class="card1" style="width: 18rem;">
            <img src='${kitablar[random].src}'class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">${kitablar[random].bookname}</h5>
                <p class="card-text">${kitablar[random].outhor}</p>
                <a href="product.html" class="btn btn-primary">Etrafli</a>
            </div></div>`
            $(".grid").append(add)
            condition=false       


        }
    }
    

})
$("#lastalert").hide()
$(".dwn").click(()=>{
    $(".col-4:last-child").remove()
})
$("#baslabtn").click(()=>{
   if( $("#lastalert").is(":hidden")){
    $("#baslabtn").attr("style","background-color:red !important")
    $("#lastalert").show()

   }
   else{
    $("#lastalert").hide()
    $("#baslabtn").attr("style","background-color:yellow !important")
   }
})
$("#hesabla").click(()=>{
    var pages=$("#pagess").val()
    var days=$("#day").val()
    var gun= parseInt(pages)/parseInt(days)
    $("#lastalert .alert").attr("style","display:flex !important")
    if (isNaN(gun)){
      $("#lastalert .alert").addClass('bg-danger')
      $(".alert p").text("hesablamada xeta baw verdi")
      $("#lastalert .alert").attr("style","display:flex !important")
    }
    else{
      $("#gun").text(`${parseInt(gun)}`)
    }
   
    
  

})
$(".hms").click(()=>{
  $(".grid-item").css("display","flex")
})
$(".rmn").click(()=>{

  
  $(".roman").attr("style","display:flex !important")
  $(".psixalogiya").attr("style","display:none !important")
 
  $(".bilim-kurgu").attr("style","display:none !important")
  $(".bilim-kurgu").attr("style","display:none !important")
  

  
})
$(".blm").click(()=>{
  $(".bilim-kurgu").attr("style","display:flex !important")
  $(".roman").attr("style","display:none !important")
  $(".psixalogiya").attr("style","display:none !important")
 
})
$(".psx").click(()=>{
  $(".psixalogiya").attr("style","display:flex !important")
  $(".roman").attr("style"," display:none !important")
  $(".bilim-kurgu").attr("style","display:none !important")
  $(".roman").attr("style"," display:none !important")
})

