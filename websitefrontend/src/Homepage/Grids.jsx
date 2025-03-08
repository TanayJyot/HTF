import React from 'react';
import img1 from './data/DSC02113 1.webp'
import img2 from './data/DSC02091 1.webp'
import img3 from './data/DSC02133 2.webp'
import img4 from './data/DSC02214 1.webp'
import heart from './data/heart.svg'
import img21 from './data/a206c0a02858ce417567e2db6a281ec8.webp'
import img22 from './data/DSC02101.webp'
import img23 from './data/DSC02137.webp'
import img24 from './data/DSC02190.webp'

const Grids = ({ second }) => {
    const items = [
        {
            id: 1,
            img: img1,
            name: "Kurti 1",
            price: 15208,
        }, {
            id: 2,
            img: img2,
            name: "Kurti 2",
            price: 1500,
        }, {
            id: 3,
            img: img3,
            name: "Kurti 3",
            price: 1200,
        }, {
            id: 4,
            img: img4,
            name: "Kurti 4",
            price: 1200,
        }, {
            id: 5,
            img: img1,
            name: "Kurti 1",
            price: 15208,
        }, {
            id: 6,
            img: img2,
            name: "Kurti 1",
            price: 1500,
        }, {
            id: 7,
            img: img3,
            name: "Kurti 1",
            price: 1200,
        }, {
            id: 8,
            img: img4,
            name: "Kurti 1",
            price: 1200,
        },
    ]

        const items2 = [
        {
            id: 1,
            img: img21,
            name: "Kurti 1",
            price: 15208,
        }, {
            id: 2,
            img: img22,
            name: "Kurti 2",
            price: 1500,
        }, {
            id: 3,
            img: img23,
            name: "Kurti 3",
            price: 1200,
        }, {
            id: 4,
            img: img24,
            name: "Kurti 4",
            price: 1200,
        }, {
            id: 5,
            img: img21,
            name: "Kurti 1",
            price: 15208,
        }, {
            id: 6,
            img: img22,
            name: "Kurti 2",
            price: 1500,
        }, {
            id: 7,
            img: img23,
            name: "Kurti 3",
            price: 1200,
        }, {
            id: 8,
            img: img24,
            name: "Kurti 4",
            price: 1200,
        },
    ]
    const using = second ? items2 : items;


    return (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mb-16 mx-5">
            {using.map((item) => (
                <div className="card card-compact w-full bg-base-100 shadow-xl relative h-[28rem]">
                    <figure className="relative">
                        <img src={item.img} className="w-full" alt="kjd"/>
                        <div className="card-actions justify-end absolute top-4 right-4">
                            <button className="btn btn-circle btn-sm">
                                <img src={heart} alt="" className="w-6 h-6"/>
                                {/*<svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none"*/}
                                {/*     viewBox="0 0 24 24" stroke="currentColor">*/}

                            </button>
                        </div>
                    </figure>

                    <div className="w-full">
                        <div className="flex flex-row justify-between p-3">
                            <p className="font-josephin font-semibold"> {item.name}</p>
                            <p> Rs.{item.price}/-</p>
                        </div>
                        {/*<div className="card-actions">*/}
                        <button className="card-body btn w-full bg-[#292D32] font-josephin text-white">Add to cart</button>
                        {/*</div>*/}
                    </div>
                </div>
            ))}
        </div>
    );
};

export default Grids;
