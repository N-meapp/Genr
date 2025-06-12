
function openUpdateModalgallery(id, category, imageUrl) {
  const form = document.querySelector('#updateGalleryForm'); // Use unique ID for update form
  const categoryInput = document.querySelector('#categoryupdate');
  const imagePreview = document.querySelector('#imagePreview');

  // Set form action dynamically
  form.action = `/updating_gallery/${id}/`;

  // Populate the category dropdown
  categoryInput.value = category || ''; // Default to empty string if null/undefined

  // Update the image preview

}




  function openUpdateModaloffer(id, title, content, imageUrl) {
    const form = document.querySelector('#offerFormupdate');
    const titleInput = document.querySelector('#offertitle');
    const contentInput = document.querySelector('#offercontent');
  
    // Set form action URL dynamically
    form.action = `/updating_offer/${id}/`;
  
    // Populate the modal fields
    titleInput.value = title || ''; // Default to empty string if null/undefined
    contentInput.value = content || ''; // Default to empty string if null/undefined
  }


  function openUpdateModalcareer(id, jobtitle, jobcontent,worktime, jobemail, phonenumber) {
    const form = document.querySelector('#careerFormupdate'); 
    const careertitleInput = document.querySelector('#jobtitle');
    const careercontentInput = document.querySelector('#jobcontent');
    const worktimeInput = document.querySelector('#worktime');
    const careeremailInput = document.querySelector('#email');
    const phoneInput = document.querySelector('#phone');


    // Update form action dynamically
    form.action = `/update_careersection/${id}/`;

    // Populate the form inputs
    careertitleInput.value = jobtitle || ''; 
    careercontentInput.value = jobcontent || ''; 
    careeremailInput.value = jobemail || ''; 
    phoneInput.value = phonenumber || '';
    worktimeInput.value = worktime || '';

}


function openUpdateModalcount(id, expert_workers, projects_done, happy_customers) {
  const form = document.querySelector('#updatecountForm');
  const happy_customersInput = document.querySelector('#happy_customers');
  const projects_doneInput = document.querySelector('#projects_done');
  const expert_workersInput = document.querySelector('#expert_workers');


  // Set form action URL dynamically
  form.action = `/updating_count/${id}/`;

  // Populate the modal fields
  happy_customersInput.value = happy_customers || ''; // Default to empty string if null/undefined
  projects_doneInput.value = projects_done || ''; // Default to empty string if null/undefined
  expert_workersInput.value = expert_workers || '';
}















// function openUpdateModalworks(id, title, category, imageUrl,description) {
//     console.log('ID:', id);
//     console.log('Title:', title);
//     console.log('Image URL:', imageUrl);
//     console.log('description:', description);


//     const form = document.querySelector('#workForm');
//     const titleInput = document.querySelector('#worktitle');
//     const categoryInput = document.querySelector('#browsers');
//     const image = document.querySelector('#workimage');
//     const descriptionInput = document.querySelector('#workdescription');



//     form.action = `/updating_works/${id}/`;

    
//     titleInput.value = title ? title : '';
//     categoryInput.value = category ? category : ''; 
//     descriptionInput.value = description ? description : ''; 

// }







function openUpdateModalworks(id, title, category, imageUrl, description, additionalImagesData) {
  const form = document.querySelector('#workForm');
  const titleInput = document.querySelector('#worktitle');
  const categoryInput = document.querySelector('#workcategory');
  const descriptionInput = document.querySelector('#workdescription');
  const existingImagesContainer = document.querySelector('#existingImages');

  // Set form action URL dynamically
  form.action = `/updating_works/${id}/`;

  // Populate primary fields
  titleInput.value = title || '';
  categoryInput.value = category || '';
  descriptionInput.value = description || '';

  // Parse the additional images data (JSON string to JavaScript object)
  let additionalImages = [];
  if (additionalImagesData) {
      try {
          additionalImages = JSON.parse(additionalImagesData);
      } catch (e) {
          console.error("Error parsing additional images data", e);
      }
  }

  // Populate existing images with checkboxes for deletion
  existingImagesContainer.innerHTML = ''; // Clear previous content
  if (additionalImages && additionalImages.length > 0) {
      additionalImages.forEach(img => {
          const imgElement = document.createElement('div');
          imgElement.classList.add('d-flex', 'align-items-center', 'mb-2');
          imgElement.innerHTML = `
              <img src="${img.image_url || img}" alt="Additional Image" style="width: 100px; height: auto; margin-right: 10px;">
              <input type="checkbox" name="delete_images" value="${img.id || img}" /> Delete
          `;
          existingImagesContainer.appendChild(imgElement);
      });
  }
}









    function showOfferFunction(fade) {
      const area = document.getElementById(`${fade}`);
      const arrayArea = document.getElementsByClassName('table-content')
      const tab = document.getElementById(`${fade}-id`)
      const navItem = document.getElementsByClassName('nav-item')
      console.log(navItem[1],'6y6t');

      for (let i = 0; i < navItem.length; i++) {
        if(navItem[i].id == tab.id) {
            navItem[i].style.background = 'rgba(14, 35, 56, 0.88)'
            navItem[i].style.color = 'rgba(250, 250, 250, 0.88)'
          }
        else{
          navItem[i].style.background = 'none'
          navItem[i].style.color = 'black'
        }
      }

      console.log(tab,'taaaaaab');
      


    console.log(area.id);

    for (let i = 0; i < arrayArea.length; i++) {
        console.log(arrayArea[i].id);
        
        if (area.id == arrayArea[i].id) {
            console.log(true);
            arrayArea[i].style.display = 'block'; 
        }
        else{
            arrayArea[i].style.display = 'none'; 
        }
    }
  }


  function showworkFunction(work_categories) {
    const workArea = document.getElementById(`${work_categories}`);
    const arrayWork = document.getElementsByClassName('work-area')


  console.log(workArea.id);

  for (let i = 0; i < arrayWork.length; i++) {
      console.log(arrayWork[i].id);
      
      if (workArea.id == arrayWork[i].id) {
          console.log(true);
          arrayWork[i].style.display = 'block'; 
      }
      else{
        arrayWork[i].style.display = 'none'; 
      }
  }
}

function showgalleryFunction(gallery_categories) {
  const galleryArea = document.getElementById(`${gallery_categories}`);
  const arrayGallery = document.getElementsByClassName('gallery-area')


console.log(galleryArea.id);

for (let i = 0; i < arrayGallery.length; i++) {
    console.log(arrayGallery[i].id);
    
    if (galleryArea.id == arrayGallery[i].id) {
        console.log(true);
        arrayGallery[i].style.display = 'block'; 
    }
    else{
      arrayGallery[i].style.display = 'none'; 
    }
}
}



function confirmDelete(jobId) {
  if (confirm("Are you sure you want to delete this job application?")) {
      document.getElementById('delete-form-' + jobId).submit();
  }
}





function openUpdateModalpackage(id, name, description) {
  const form = document.querySelector('#packageFormupdate');
  const titleInput = document.querySelector('#name');
  const contentInput = document.querySelector('#description');

  // Set form action URL dynamically
  form.action = `/updating_package/${id}/`;

  // Populate the modal fields
  titleInput.value = name || ''; // Default to empty string if null/undefined
  contentInput.value = description || ''; // Default to empty string if null/undefined
}


  
function showproductFunction(package_categories) {
  const packageArea = document.getElementById(`${package_categories}`);
  const arrayPackage = document.getElementsByClassName('packagearea')


console.log(packageArea.id);

for (let i = 0; i < arrayPackage.length; i++) {
    console.log(arrayPackage[i].id);
    
    if (packageArea.id == arrayPackage[i].id) {
        console.log(true);
        arrayPackage[i].style.display = 'block'; 
    }
    else{
      arrayPackage[i].style.display = 'none'; 
    }
}
}




  const brandModal = document.getElementById('brandModal');
  brandModal.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget; // Button that triggered the modal
    const productId = button.getAttribute('data-product-id'); // Extract product ID from data-product-id
    
    // Set the product ID in the hidden input field
    document.getElementById('modalProductId').value = productId;
  });
