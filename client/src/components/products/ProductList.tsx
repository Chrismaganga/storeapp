// src/components/ProductList.js
import React from 'react';
import useProducts from './useProducts';


const ProductList = () => {
  const { products, loading, error } = useProducts('http://127.0.0.1:8000/api/products/');

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error fetching products: {error.message}</p>;

  return (
    <div className=' border-solid'>
      <h1 className='text-center justify-center text-red-600 uppercase  '>Product List</h1>
      <ul className='grid grid-rows-2 grid-flow-col gap-4  justify-between'>
        {products.map(product => (
          <li key={product.id}>
            <h2 className='text-center justify-center text-blue-700'>{product.name}</h2> 
            <p className='items-center'>{product.content}</p>
            <div className='rounded-lg items-center'>
              {product.image && (
                <img src={product.image} alt={product.name} style={{ width: '300px', height: '300px' }} className='rounded-lg'/>
              )}
            </div>
            <p className='text-center justify-center'>Price: ${product.price}</p>
            <p className='text-center'>Sale Price: ${product.sale_price}</p>
            <p className='text-center'>Discount: ${product.my_discount}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;
