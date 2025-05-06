// Company search functionality
$(document).ready(function () {
    $("#searchInput").autocomplete({
        source: function (request, response) {
            $.ajax({
                url: "/autocomplete",  // Use relative path (Flask will handle it)
                data: { term: request.term },
                success: function (data) {
                    response(data);
                }
            });
        },
        minLength: 1,  // Minimum characters before suggestions appear
    });

    // Ensure search input is not empty before submitting
    $("#searchForm").on("submit", function () {
        let searchValue = $("#searchInput").val().trim();
        if (searchValue === "") {
            alert("Please enter a search term.");
            return false;
        }
    });

    // Favorite button logic (localStorage-based)
    const favoriteButtons = document.querySelectorAll(".favorite-btn");

    favoriteButtons.forEach(btn => {
        const itemId = btn.dataset.id;

        // Restore state from localStorage
        if (localStorage.getItem(`favorite-${itemId}`) === "true") {
            btn.classList.add("favorited");
            btn.innerText = "★ Favorited";
        }

        btn.addEventListener("click", () => {
            const isFavorited = btn.classList.toggle("favorited");
            btn.innerText = isFavorited ? "★ Favorited" : "☆ Favorite";

            // Save state in localStorage
            localStorage.setItem(`favorite-${itemId}`, isFavorited);
        });
    });

    // Fix back button cache issue (optional)
    window.addEventListener("pageshow", function (event) {
        if (event.persisted) {
            window.location.reload();
        }
    });
    
});
