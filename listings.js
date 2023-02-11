
fetch('listings.json')
    .then(response => response.json())
    .then(data => {
        data.forEach(item => {
            let parentDiv = document.getElementById("listings");

            let childDiv = document.createElement("div");
            childDiv.classList.add("child-div");
        
            let image = document.createElement("img");
            image.src = item.image;
            childDiv.appendChild(image);
        
            let title = document.createElement("h3");
            title.innerHTML = item.title;
            childDiv.appendChild(title);
        
            let button = document.createElement("button");
            button.innerHTML = "Purchase $" + item.price;
            button.onclick = function() {
                window.open(item.url, "_blank");
            };
            childDiv.appendChild(button);

            childDiv.className = "image fit";
        
            parentDiv.appendChild(childDiv);
        });
    });
