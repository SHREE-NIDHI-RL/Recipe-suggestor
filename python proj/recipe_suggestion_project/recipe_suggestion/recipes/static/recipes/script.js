const dummyRecipes = [
    { name: "Tomato Pasta", ingredients: ["tomato", "pasta"], cuisine: "Italian" },
    { name: "Egg Fried Rice", ingredients: ["egg", "rice", "soy sauce"], cuisine: "Asian" },
    { name: "Grilled Cheese", ingredients: ["bread", "cheese", "butter"], cuisine: "American" },
  ];
  /*
  function searchRecipes() {
    const input = document.getElementById("ingredientInput").value.toLowerCase();
    const ingredients = input.split(",").map(i => i.trim());
    const container = document.getElementById("recipeResults");
    container.innerHTML = "";
  
    const results = dummyRecipes.filter(recipe =>
      ingredients.every(ing => recipe.ingredients.includes(ing))
    );
  
    if (results.length === 0) {
      container.innerHTML = "<p style='text-align:center;'>No recipes found.</p>";
      return;
    }
  
    results.forEach(recipe => {
      const card = document.createElement("div");
      card.className = "recipe-card";
      card.innerHTML = `
        <h3>${recipe.name}</h3>
        <p><strong>Cuisine:</strong> ${recipe.cuisine}</p>
        <p><strong>Ingredients:</strong> ${recipe.ingredients.join(", ")}</p>
      `;
      container.appendChild(card);
    });
  }*/
    function searchRecipes() {
      const ingredient = document.getElementById('ingredientInput').value;
      fetch(`/search-recipes/?ingredient=${ingredient}`)
          .then(response => response.json())
          .then(data => {
              const resultsContainer = document.getElementById('recipeResults');
              resultsContainer.innerHTML = ''; // Clear previous results
              data.forEach(recipe => {
                  const recipeElement = document.createElement('div');
                  recipeElement.classList.add('recipe');
                  recipeElement.innerHTML = `
                      <h3>${recipe.name}</h3>
                      <p>${recipe.cuisine}</p>
                      <p>${recipe.ingredients}</p>
                      <a href="/recipe/${recipe.id}">View Recipe</a>
                  `;
                  resultsContainer.appendChild(recipeElement);
              });
          });
  }
  