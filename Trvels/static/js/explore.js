document.getElementById("budgetFilter").addEventListener("input", function () {
  let budget = this.value;
  document.getElementById("budgetValue").textContent =
    "₹" + budget.toLocaleString();
  applyFilters();
});

document
  .getElementById("locationFilter")
  .addEventListener("change", applyFilters);

function applyFilters() {
  let maxBudget = document.getElementById("budgetFilter").value;
  let selectedLocation = document.getElementById("locationFilter").value;

  document.querySelectorAll(".destination-card").forEach((card) => {
    let cardPrice = parseInt(card.getAttribute("data-price"));
    let cardLocation = card.getAttribute("data-location");

    if (
      cardPrice <= maxBudget &&
      (selectedLocation === "all" || selectedLocation === cardLocation)
    ) {
      card.style.display = "block";
    } else {
      card.style.display = "none";
    }
  });
}
