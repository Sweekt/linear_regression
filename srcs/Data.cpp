#include "Data.hpp"

// Constructors & destructor
Data::Data(void) {
    std::cout << "Data default constructor called!" << std::endl;
}

Data::Data(const Data &copy) {
    std::cout << "Data copy constructor called!" << std::endl;
    *this = copy;
}

Data::~Data(void) {
    std::cout << "Data default destructor called!" << std::endl;
}

// Overloaded operators
Data &Data::operator=(const Data &src) {
    if (this != &src) {

    }
    return (*this);
}

// Public methods
