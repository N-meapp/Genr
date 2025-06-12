
(function ($) {
  "use strict";

  // Spinner
  var spinner = function () {
    setTimeout(function () {
      if ($("#spinner").length > 0) {
        $("#spinner").removeClass("show");
      }
    }, 1);
  };
  spinner();

  // Initiate the wowjs
  new WOW().init();

  // Sticky Navbar
  $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
      $(".sticky-top").addClass("shadow-sm").css("top", "0px");
    } else {
      $(".sticky-top").removeClass("shadow-sm").css("top", "-100px");
    }
  });

  // Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 300) {
      $(".back-to-top").fadeIn("slow");
    } else {
      $(".back-to-top").fadeOut("slow");
    }
  });
  $(".back-to-top").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1500, "easeInOutExpo");
    return false;
  });

  // Facts counter
  $('[data-toggle="counter-up"]').counterUp({
    delay: 10,
    time: 2000,
  });

  // Header carousel
  $(".header-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1500,
    loop: true,
    nav: false,
    dots: true,
    items: 1,
    dotsData: true,
  });

  // Testimonials carousel
  $(".testimonial-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1000,
    center: true,
    dots: false,
    loop: true,
    nav: true,
    navText: [
      '<i class="bi bi-arrow-left"></i>',
      '<i class="bi bi-arrow-right"></i>',
    ],
    responsive: {
      0: {
        items: 1,
      },
      768: {
        items: 2,
      },
    },
  });

  // Portfolio isotope and filter
  var portfolioIsotope = $(".portfolio-container").isotope({
    itemSelector: ".portfolio-item",
    layoutMode: "fitRows",
  });
  $("#portfolio-flters li").on("click", function () {
    $("#portfolio-flters li").removeClass("active");
    $(this).addClass("active");

    portfolioIsotope.isotope({ filter: $(this).data("filter") });
  });
})(jQuery);

// offersection

const sliderControls = document.querySelector(".slider-controls");
const sliderTabs = sliderControls.querySelectorAll(".slider-tab");
const sliderIndicator = sliderControls.querySelector(".slider-indicator");

// Update the indicator
const updateIndicator = (tab, index) => {
  document.querySelector(".slider-tab.current")?.classList.remove("current");
  tab.classList.add("current");

  sliderIndicator.style.transform = `translateX(${tab.offsetLeft - 20}px)`;
  sliderIndicator.style.width = `${tab.getBoundingClientRect().width}px`;

  // Calculate the scroll position and scroll smoothly
  const scrollLeft =
    sliderTabs[index].offsetLeft -
    sliderControls.offsetWidth / 2 +
    sliderTabs[index].offsetWidth / 2;
  sliderControls.scrollTo({ left: scrollLeft, behavior: "smooth" });
};

// Initialize swiper instance
const swiper = new Swiper(".slider-container", {
  effect: "fade",
  speed: 500,
  autoplay: { delay: 1000 },
  navigation: {
    prevEl: "#slide-prev",
    nextEl: "#slide-next",
  },
  on: {
    // Update indicator on slide change
    slideChange: () => {
      const currentTabIndex = [...sliderTabs].indexOf(
        sliderTabs[swiper.activeIndex]
      );
      updateIndicator(sliderTabs[swiper.activeIndex], currentTabIndex);
    },
    reachEnd: () => swiper.autoplay,
  },
});

// Update the slide on tab click
sliderTabs.forEach((tab, index) => {
  tab.addEventListener("click", () => {
    swiper.slideTo(index);
    updateIndicator(tab, index);
  });
});

updateIndicator(sliderTabs[0], 0);
window.addEventListener("resize", () =>
  updateIndicator(sliderTabs[swiper.activeIndex], 0)
);

// add field

function addNewRow() {
  const tbody = document.getElementById("appliances-body");
  const newRow = document.createElement("tr");

  newRow.innerHTML = `
        <td><input type="text" placeholder="New Appliance"></td>
        <td><input type="text" placeholder="Units"></td>
        <td>X</td>
        <td><input type="text" placeholder="Counts"></td>
        <td>=</td>
        <td><input type="text" placeholder="Load"></td>
        <td><button class="action-btn" onclick="addNewRow()">Add</button></td>
    `;

  tbody.insertBefore(newRow, tbody.querySelector(".total-row"));
}

function handleLoadCalc(value, firstValueId, secondValueId, outputId) {
  
  const secondValueEl = document.getElementById(secondValueId);
  const secondValue = secondValueEl.value;
  const firstValueEl = document.getElementById(firstValueId);
  const firstValue = firstValueEl.value;
  const output = document.getElementById(outputId);
  const getAllLoad = document.getElementsByClassName("loadcalc-load");
  const totalLoad = document.getElementById("total-load");
  const totalLoadInKw = document.getElementById("total-load-in-kw");

  output.style.fontWeight = 'bold';
  output.style.color = 'black';
  output.style.fontSize = 'medium'

  if (firstValue && secondValue) {
    if (isNaN(value * secondValue)) {
      console.log("dddd");

      output.value = "Enter the values";
      output.style.fontWeight = '300';
      output.style.color = '#ff000078';
      output.style.fontSize = 'small'
    } else {
      output.value = value * secondValue;

      console.log(value * secondValue,'fddfdfdf');
      
     
    }
  } else {
    output.value = null;
  }
  let temp = 0;
  for (let i = 0; i < getAllLoad.length; i++) {
    temp += +getAllLoad[i].value;
  }
  
  if(!isNaN(temp)){
    totalLoad.value = temp;
    totalLoadInKw.value = temp / 1000;
  }
}

function addAppliances() {
  const appliancesList = document.getElementById("appliances-list");

  const newRow = document.createElement("tr");

  const randomId = generateRandom6DigitNumber();
  const xId = generateRandom6DigitNumber();
  const countsId = generateRandom6DigitNumber();
  const loadId = generateRandom6DigitNumber();

  newRow.setAttribute("id", randomId);

  newRow.innerHTML = `
            <td><input
                class="text-center py-2 non-input"
                placeholder="type here..."
                type="text"
              /></td>
            <td>other</td>
            <td>
              <input
                class="text-center Rounded py-2 border"
                id=${xId}
                onchange="handleLoadCalc(event.target.value,${xId},${countsId},${loadId})"
                type="text"
              />
            </td>
            <td>
              <input
                class="text-center Rounded py-2 border"
                id=${countsId}
                onchange="handleLoadCalc(event.target.value,${countsId},${xId},${loadId})"
                type="text"
              />
            </td>
            <td>=</td>
            <td>
              <input
                class="text-center Rounded py-2 loadcalc-load"
                id=${loadId}
                type="text"
                disabled
              />
            </td>
            <td>
              <div class="applience-closing" onclick="closeAppliances(${randomId})">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="black" class="size-4">
  <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14Zm2.78-4.22a.75.75 0 0 1-1.06 0L8 9.06l-1.72 1.72a.75.75 0 1 1-1.06-1.06L6.94 8 5.22 6.28a.75.75 0 0 1 1.06-1.06L8 6.94l1.72-1.72a.75.75 0 1 1 1.06 1.06L9.06 8l1.72 1.72a.75.75 0 0 1 0 1.06Z" clip-rule="evenodd" />
</svg>


              </div>
            </td>`;

  appliancesList.appendChild(newRow);
}

function closeAppliances(id) {
  const closingRow = document.getElementById(id);
  const totalLoad = document.getElementById("total-load");
  const totalLoadInKw = document.getElementById("total-load-in-kw");

  closingValue = getSeventhChildValue(id);

  if (closingRow) {
    closingRow.remove();
    console.log("hahahha", totalLoad.value, closingValue);

    if(!isNaN(closingValue)){
      const total = totalLoad.value - closingValue;
      totalLoad.value = total;
      totalLoadInKw.value = total / 1000;
    }
  }
}

function generateRandom6DigitNumber() {
  return Math.floor(100000 + Math.random() * 900000);
}

function getSeventhChildValue(id) {
  const row = document.getElementById(id);

  console.log(row.children);

  if (row) {
    // Access the 7th child element
    const seventhChild = row.children[5].children[0]; // Index is 0-based, so 6 refers to the 7th child
    if (seventhChild) {
      const value = seventhChild.value;
      console.log(value, "thisis  "); // Display the value in the console
      return value;
    } else {
      console.log("7th child not found");
    }
  } else {
    console.log("Row not found");
  }
}


function activeTabs(fade) {
  const tab = document.getElementById(fade);
  const navItems = document.getElementsByClassName('nav-link');

  for (let i = 0; i < navItems.length; i++) {
    if (navItems[i].id === tab.id) {
      navItems[i].classList.add('active'); // Add active class
      navItems[i].style.background = 'rgba(14, 35, 56, 0.88)';
      navItems[i].style.color = 'rgba(250, 250, 250, 0.88)';
    } else {
      navItems[i].classList.remove('active'); // Remove active class
      navItems[i].style.background = 'none';
      navItems[i].style.color = 'black';
    }
  }

  console.log(tab, 'Activated tab');
}






// drop down js
 



