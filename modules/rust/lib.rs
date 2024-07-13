use pyo3::prelude::*;

#[pyfunction]
fn get_free_id(range_from:u64, range_til:u64) -> u32 {
    if (self.__data.get(self.__table)){
        datas_id = set(data.get("id") for data in self.__data.get(self.__table))
        ids = list(set([item for item in range(min(datas_id) - min(datas_id) + 1, max(datas_id) + 1)]).difference(datas_id))
        return ids.pop() if len(ids) > 0 else max(datas_id) + 1
    }
    return 1
}

#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_free_id, m)?)?;
    Ok(())
}