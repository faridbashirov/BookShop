const heartBtn=document.getElementById("heartbtn")
const elaveEt=document.getElementById("sebetelvt")
const modal=document.getElementById("sebetalert")
const modalclose=document.getElementById("alertclosebutton")
const bookname=document.getElementById("bookname")
const bookprice=document.getElementById("incognito")
const ktbAdlr=document.getElementById("ktbadlr")
const delETE=document.querySelectorAll(".delete")
const allprice=document.querySelectorAll(".allprice")[0]
const sebetndcx=document.getElementById("sebetdncx")
const k1984=document.getElementById("k1984")
const sefiller=document.getElementById("sefiller")
const radius=document.getElementById("radius")
const alerts=document.getElementById("alert")
const like=document.getElementById("like")
const unlike=document.getElementById("unlike")
const regex = /\d+/g;
alerts.innerText.match(regex)
var cem=0

like.addEventListener("click",()=>{
    like.style.display="none"
    unlike.style.display="inline-block"
})
unlike.addEventListener("click",()=>{
    like.style.display="inline-block"
    unlike.style.display="none"
})


if (parseInt(ktbAdlr.childElementCount)===0){
    radius.style.display="none"
}
else{
    radius.innerText=parseInt(ktbAdlr.childElementCount)
}


for(var i =0;i<delETE.length;i++){
    var x=delETE[i]
   
    x.addEventListener("click",(event)=>{
       event.target.parentElement.parentElement.parentElement.remove()
       if (parseInt(ktbAdlr.childElementCount)===0){
        radius.style.display="none"
    }
    else{
        radius.innerText=parseInt(ktbAdlr.childElementCount)
    }
    

       cem=parseInt(allprice.innerText.match(regex))
       cem-=parseInt(event.target.parentElement.nextElementSibling.innerText.match(regex)[0])
       allprice.innerText=`${cem} AZN`
        
       
       
    })

}

heartBtn.style.color="gray"
heartBtn.addEventListener("click",()=>{
    if (heartBtn.style.color ==="gray"){
        alert("KITABI BEYENDINIZ!")
        heartBtn.style.color="red"
    }
    else{
        heartBtn.style.color="gray"
        alert("KITABI BEYENMEDINIZ")
    }
    
    
})
elaveEt.addEventListener("click",()=>{
ktbAdlr.innerHTML+=`<li class="sey" id='inco'><a class=" dropdowna dropdown-item sey" href="#"> <span><i id='inc_x' class="delete fa-thin fa-x text-danger"></i> ${bookname.innerText} </span> <span class="ktbprice"> ${bookprice.innerText}</span></a></li>`
elaveEt.style.display="none"
sebetndcx.style.display="inline-block"
const delETE=document.querySelectorAll(".delete")
const radius=document.getElementById("radius")
radius.style.display="block"
for(var i =0;i<delETE.length;i++){
    var x=delETE[i]
    x.addEventListener("click",(event)=>{

        if(event.target===document.getElementById('inc_x')){
            
            sebetndcx.style.display="none"
            elaveEt.style.display="inline-block"
            var qaliq=alerts.innerText.match(regex)
        
            qaliq=(parseInt(qaliq))+1
            alerts.innerText=`Bu kitabdan ${qaliq} eded qalib.`
            alerts.classList.replace("alert-danger","alert-warning")

        }
     
       
        
       event.target.parentElement.parentElement.parentElement.remove()
       if (parseInt(ktbAdlr.childElementCount)===0){
        radius.style.display="none"
    }
    else{
        radius.innerText=parseInt(ktbAdlr.childElementCount)
    }
    //    radius.style.display="block"
    //    radius.innerText=parseInt(ktbAdlr.childElementCount)
       cem=parseInt(allprice.innerText.match(regex))
        cem-=parseInt(event.target.parentElement.nextElementSibling.innerText.match(regex)[0])
        allprice.innerText=`${cem} AZN`
        
       
    })

}
   sebetndcx.addEventListener("click",(event)=>{
        document.getElementById("inco").remove()
        sebetndcx.style.display="none"
        elaveEt.style.display="inline-block"
        cem=parseInt(allprice.innerText.match(regex))
        cem-=parseInt(bookprice.innerText.match(regex))
        allprice.innerText=`${cem} AZN`
        radius.innerText=parseInt(ktbAdlr.childElementCount)
        var qaliq=alerts.innerText.match(regex)
        
        qaliq=(parseInt(qaliq))+1
        alerts.innerText=`Bu kitabdan ${qaliq} eded qalib.`
        alerts.classList.replace("alert-danger","alert-warning")
        if (parseInt(ktbAdlr.childElementCount)===0){
            radius.style.display="none"
        }
        else{
            radius.innerText=parseInt(ktbAdlr.childElementCount)
        }
    
       
        
     })

modal.style.display="block"
    
    cem=parseInt(allprice.innerText.match(regex))
    cem+=parseInt(bookprice.innerText.match(regex))
    allprice.innerText=`${cem} AZN`
    radius.innerText=parseInt(ktbAdlr.childElementCount)
     var qaliq=alerts.innerText.match(regex)
        qaliq-=1
        alerts.innerText=`Bu kitabdan ${qaliq} eded qalib.`
        if (qaliq<=1){
            alerts.classList.replace("alert-warning","alert-danger")
           
        }
    
    modalclose.addEventListener("click",()=>{
       modal.style.display="none"
       
    })
    
})
$("#hesabla").click(()=>{
    var pages=$("#pagess").val()
    console.log(pages)
    var days=$("#dayss")
    var gun= (pages/days)
    console.log(gun)
    $("#gun").val()=gun

})
$(".hms").click(()=>{
    $(".")
})

