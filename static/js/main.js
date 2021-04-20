const burger = document.getElementById("hamburger"),
      closeBurger = document.getElementById("close-burger"),
      menu = document.getElementById("menu"),
      body = document.querySelector("body"),
      toggleItemList = document.querySelectorAll(".toglle-item__list"),
      toggleItems = document.querySelectorAll(".toglle-item");

let activeElem;

closeBurger.addEventListener('click',()=>{
  menu.classList.remove('mob-header--active');
  body.classList.remove('hide');
})

burger.addEventListener('click',e=>{
    menu.classList.add('mob-header--active');
    body.classList.add('hide');
});


function clearAllItems(){
  toggleItemList.forEach(toggleItemList=>{
    toggleItemList.classList.remove('toglle-item__list--active');
    
  })
  toggleItems.forEach(toggleItem=>{
    toggleItem.classList.remove('toglle-item--active');
    let text = toggleItem.querySelector('.hero__description-text');
    text.classList.remove('hero__description-text--active');
  })
}


function visibleOneItem(itemId){
  clearAllItems();
  if (activeElem == itemId){
    toggleItemList[itemId].classList.remove('toglle-item__list--active');
    toggleItems[itemId].classList.remove('toglle-item--active');
    let text = toggleItems[itemId].querySelector('.hero__description-text');
    text.classList.remove('hero__description-text--active');
    activeElem = -1;
  }
  else{
    activeElem = itemId;
    toggleItemList[itemId].classList.add('toglle-item__list--active');
    toggleItems[itemId].classList.add('toglle-item--active');
    let text = toggleItems[itemId].querySelector('.hero__description-text');
    text.classList.add('hero__description-text--active');
  }
  
}

toggleItems.forEach((toggleItem,i)=>{
  toggleItem.addEventListener('click',tIC=>{
    visibleOneItem(i);
  });
});
