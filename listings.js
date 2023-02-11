
fetch('listings.json')
    .then(response => response.json())
    .then(data => {
        data.forEach(item => {
            let parentDiv = document.getElementById("listings");

            let childDiv = document.createElement("div");
            childDiv.classList.add("child-div");
        
            let image = document.createElement("img");
            image.src = item.image;
        
            let title = document.createElement("h3");
            title.innerHTML = item.title;
        
            let button = document.createElement("button");
            button.innerHTML = "Learn More";
            button.onclick = function() {
                window.open(item.url, "_blank");
            };

            childDiv.appendChild(image);
            childDiv.appendChild(title);
            childDiv.appendChild(button);

            childDiv.className = "image fit";
            childDiv.style.borderBottom = "1px solid lightgrey";
            childDiv.style.paddingBottom = "10px";

            parentDiv.appendChild(childDiv);
        });
    });
