function rgb(r, g, b) {
    r = Math.max(0, Math.min(255, Math.round(r)));
    g = Math.max(0, Math.min(255, Math.round(g)));
    b = Math.max(0, Math.min(255, Math.round(b)));

    const hexR = r.toString(16).padStart(2, "0").toUpperCase();
    const hexG = g.toString(16).padStart(2, "0").toUpperCase();
    const hexB = b.toString(16).padStart(2, "0").toUpperCase();

    return hexR + hexG + hexB;
}