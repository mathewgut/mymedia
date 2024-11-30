const ratingSpan = document.getElementById('item-rating')



if(Number(ratingSpan.textContent) <= 5.5){
    ratingSpan.style.color = "rgb(255, 0, 0)"
}
else if(ratingSpan.textContent > 5.5 && ratingSpan.textContent <= 6.5){
    ratingSpan.style.color = "rgb(191, 64, 128)"
} else if(ratingSpan.textContent > 6.5 && ratingSpan.textContent <= 7){
    ratingSpan.style.color = "rgb(128, 128, 191)"
} else if(ratingSpan.textContent > 7 && ratingSpan.textContent <= 7.7){
    ratingSpan.style.color = "rgb(118,215,62)"
} else if(ratingSpan.textContent > 7.7 && ratingSpan.textContent <= 9){
    ratingSpan.style.color = "rgb(255, 255, 0)"
}