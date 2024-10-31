use pyo3::prelude::*;

#[pyfunction]
fn extract<'py>(filename: &'py str) -> anyhow::Result<Vec<String>> {
    let doc = lopdf::Document::load(filename)?;
    let mut texts: Vec<String> = vec![];

    for (id, _) in doc.get_pages() {
        texts.push(doc.extract_text(&[id])?);
    }

    Ok(texts)
}

#[pyfunction]
fn extract_bytes(b: &[u8]) -> anyhow::Result<Vec<String>> {
    let doc = lopdf::Document::load_mem(b)?;
    let mut texts: Vec<String> = vec![];

    for (id, _) in doc.get_pages() {
        texts.push(doc.extract_text(&[id])?);
    }

    Ok(texts)
}

#[pymodule]
fn crapdf(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(extract, m)?)?;
    m.add_function(wrap_pyfunction!(extract_bytes, m)?)?;
    Ok(())
}
