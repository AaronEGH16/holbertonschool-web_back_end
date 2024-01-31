const groceriesList = () => {
  const items = [
    { name: 'Apples', quantity: 10 },
    { name: 'Tomatoes', quantity: 10 },
    { name: 'Pasta', quantity: 1 },
    { name: 'Rice', quantity: 1 },
    { name: 'Banana', quantity: 5 },
  ];
  const grocery = new Map();

  items.map(({ name, quantity }) => grocery.set(name, quantity));
  return grocery;
};

export default groceriesList;
