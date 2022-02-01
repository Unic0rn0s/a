def get_suitable_spn(toponym):
    toponym_upper_corner = [float(x) for x in toponym["boundedBy"]["Envelope"]["upperCorner"].split()]
    toponym_lower_corner = [float(x) for x in toponym["boundedBy"]["Envelope"]["lowerCorner"].split()]
    return (toponym_upper_corner[0] - toponym_lower_corner[0],
            toponym_upper_corner[1] - toponym_lower_corner[1])
