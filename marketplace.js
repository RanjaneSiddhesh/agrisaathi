const products = [
  {
    name: "Wheat",
    price: "₹ 2400 / Quintal",
    place: "Sangli",
    contact: "9876543210",
    category: "crop",
    condition: "New",
    year: "",
    img: "/static/image/wheat.png"
  },
  {
    name: "Sugarcane",
    price: "₹ 3200 / Quintal",
    place: "Kolhapur",
    contact: "9123456780",
    category: "crop",
    condition: "New",
    year: "",
    img: "/static/image/sugercane.png"
  },
  {
    name: "Soybean",
    price: "₹ 4200 / Quintal",
    place: "Satara",
    contact: "9988776655",
    category: "crop",
    condition: "New",
    year: "",
    img: "/static/image/soybean.png"
  },
  {
    name: "Onion",
    price: "₹ 1800 / Quintal",
    place: "Nashik",
    contact: "9090909090",
    category: "crop",
    condition: "New",
    year: "",
    img: "/static/image/onion.png"
  },
  {
    name: "Tomato",
    price: "₹ 2200 / Quintal",
    place: "Solapur",
    contact: "9898989898",
    category: "crop",
    condition: "New",
    year: "",
    img: "https://upload.wikimedia.org/wikipedia/commons/8/89/Tomato_je.jpg"
  },

  /* EQUIPMENT */

  {
    name: "Tractor (Used)",
    price: "₹ 3,80,000",
    place: "Satara",
    contact: "9765432109",
    category: "equipment",
    condition: "Used",
    year: "2019",
    img: "/static/image/tractor.pngg"
  },
  {
    name: "Rotavator",
    price: "₹ 55,000",
    place: "Sangli",
    contact: "9345678123",
    category: "equipment",
    condition: "New",
    year: "",
    img: "/static/image/rotavator.png"
  },
  {
    name: "Sprayer Pump",
    price: "₹ 6,500",
    place: "Kolhapur",
    contact: "9556677889",
    category: "equipment",
    condition: "New",
    year: "",
    img: "/static/image/sprayerpump.png"
  },
  {
    name: "Plough (Used)",
    price: "₹ 12,000",
    place: "Pune",
    contact: "9887766554",
    category: "equipment",
    condition: "Used",
    year: "2020",
    img: "https://upload.wikimedia.org/wikipedia/commons/8/82/Ploughing_field.jpg"
  },
  {
    name: "Thresher Machine",
    price: "₹ 90,000",
    place: "Nashik",
    contact: "9012345678",
    category: "equipment",
    condition: "Used",
    year: "2018",
    img: "https://upload.wikimedia.org/wikipedia/commons/0/0a/Threshing_machine.jpg"
  }
];

const grid = document.getElementById("productGrid");

function render(list) {
  grid.innerHTML = "";
  list.forEach(p => {
    grid.innerHTML += `
      <div class="card">
        <img src="${p.img}" alt="${p.name}">
        <div class="info">
          <h3>${p.name}</h3>
          <div class="price">${p.price}</div>
          <div>📍 ${p.place}</div>
          <div>📞 ${p.contact}</div>
          <div>Condition: ${p.condition} ${p.year ? `(${p.year})` : ""}</div>
          <button onclick="alert('Contact Seller: ${p.contact}')">
            Contact Seller
          </button>
        </div>
      </div>
    `;
  });
}

render(products);

/* TOGGLE BUY / SELL */
function showSection(type) {
  buySection.classList.add("hidden");
  sellSection.classList.add("hidden");
  type === "buy"
    ? buySection.classList.remove("hidden")
    : sellSection.classList.remove("hidden");
}

/* SEARCH & FILTER */
searchBox.oninput = categoryFilter.onchange = () => {
  const text = searchBox.value.toLowerCase();
  const cat = categoryFilter.value;

  render(
    products.filter(p =>
      p.name.toLowerCase().includes(text) &&
      (cat === "all" || p.category === cat)
    )
  );
};

/* ADD PRODUCT */
function addProduct() {
  if (!sName.value || !sPrice.value || !sPlace.value || !sContact.value) {
    alert("Fill all required fields");
    return;
  }

  products.push({
    name: sName.value,
    price: sCategory.value === "crop"
      ? `₹ ${sPrice.value} / Quintal`
      : `₹ ${sPrice.value}`,
    place: sPlace.value,
    contact: sContact.value,
    category: sCategory.value,
    condition: sCondition.value,
    year: sCondition.value === "used" ? sYear.value : "",
    img: sImage.value || "https://upload.wikimedia.org/wikipedia/commons/6/6f/Wheat_close-up.JPG"
  });

  alert("Product added successfully");
  render(products);
  showSection("buy");
}
