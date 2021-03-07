import React from 'react';
import './components.css';
import { AppBar, Toolbar, Typography, Button } from '@material-ui/core';

function NavBar() {
    return (
        <div>
            <AppBar className="backgroud-color" position="static">
                <Toolbar>
                    <Typography className='align-items font-color' variant="title">
                        Population Analysis
                    </Typography>
                    <div>
                        <Button className='font-color'>
                            Home
                        </Button>
                        <Button className='font-color'>
                            About
                        </Button>
                        <Button className='font-color'>
                            Contact
                        </Button>
                    </div>
                </Toolbar>
            </AppBar>
        </div>
    )
}

export default NavBar;