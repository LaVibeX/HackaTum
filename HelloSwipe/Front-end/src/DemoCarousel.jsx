import React, { Component } from 'react';
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
import { Carousel } from 'react-responsive-carousel';

// export default function Carousel() {
//     return (
//       <div id="CarouselBox">
        
//       </div>
//     );
//   }

class DemoCarousel extends Component {
    render() {
        return (
            <Carousel>
                <div>
                    <img src="assets\Hello_Fresh_Lockup.png" />
                    <p className="legend">Legend 1</p>
                </div>
                <div>
                    <img src="assets\Hello_Fresh_Lockup.png" />
                    <p className="legend">Legend 2</p>
                </div>
                <div>
                    <img src="assets\Hello_Fresh_Lockup.png" />
                    <p className="legend">Legend 3</p>
                </div>
            </Carousel>
        );
    }
}

export default DemoCarousel