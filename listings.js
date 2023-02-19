let parentDiv = document.getElementById("listings");

fetch('http://api.natemaeysfineart.com:1024/listings')
    .then(response => response.json())
    .then(data => {
        data.forEach(item => {

            let childDiv = document.createElement("article");
            childDiv.classList.add("child-div");
        
            let aDiv = document.createElement("a")
            aDiv.className = "image fit";
            let image = document.createElement("img");
            image.src = item.image;
            aDiv.appendChild(image);
        
            let title = document.createElement("h3");
            title.innerHTML = item.title;
        
            let button = document.createElement("button");
            button.innerHTML = "Learn More";
            button.onclick = function() {
                window.open(item.url, "_blank");
            };

            childDiv.appendChild(aDiv);
            childDiv.appendChild(title);
            childDiv.appendChild(button);

            parentDiv.appendChild(childDiv);
        });
    });
